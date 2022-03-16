import numpy as np
import pylab as pl
from binary_and_hist import entropy_binary_gray_image
#kernal 必须为方阵
def binary_morphology_krnal_flip(kernal):
    kernal_row=kernal.shape[0]
    output=np.zeros([kernal_row,kernal_row])
    if kernal_row % 2==0:
        for i in range(int(kernal_row/2)):
            for j in range(kernal_row):
                output[i,j]=kernal[kernal_row-i-1,kernal_row-j-1]
                output[kernal_row-i-1,kernal_row-j-1]=kernal[i,j]
    else:
        for i in range(int(kernal_row/2)):
            for j in range(kernal_row):
                output[i, j] = kernal[kernal_row - i - 1, kernal_row - j - 1]
                output[kernal_row - i - 1, kernal_row - j - 1] = kernal[i, j]
        i=int((kernal_row+1)/2)-1
        for j in range(int(kernal_row/2)):
            output[i, j] = kernal[kernal_row - i - 1, kernal_row - j - 1]
            output[kernal_row - i - 1, kernal_row - j - 1] = kernal[i, j]
    return output

def binary_morphology_dilation(image,kernal):
    matrix_dim3 = kernal.shape[0] * kernal.shape[1]
    matrix = np.zeros([image.shape[0] + kernal.shape[0] - 1, image.shape[1] + kernal.shape[1] - 1, matrix_dim3])
    dim3_index = 0
    for i in range(kernal.shape[0]):
        for j in range(kernal.shape[1]):
            if kernal[i,j]==1:
                matrix[i:i + image.shape[0], j:j + image.shape[1], dim3_index] = image# + kernal[i, j]
                dim3_index += 1
    output_image = np.max(matrix, axis=2)
    return output_image

def binary_morphology_erosion(image,kernal):
    matrix_dim3 = kernal.shape[0] * kernal.shape[1]
    matrix1 = np.zeros([image.shape[0] + kernal.shape[0] - 1, image.shape[1] + kernal.shape[1] - 1, matrix_dim3])
    kernal_flip = binary_morphology_krnal_flip(kernal)
    dim3_index = 0
    for i in range(kernal.shape[0]):
        for j in range(kernal.shape[1]):
            if kernal[i, j] == 1:
                matrix1[i:i + image.shape[0], j:j + image.shape[1], dim3_index] = image #- kernal_flip[i, j]
                dim3_index += 1
    output_image1 = np.min(matrix1[kernal.shape[1] - 1:-kernal.shape[1] + 1, kernal.shape[0] - 1:-kernal.shape[0] + 1, 0:dim3_index], axis=2)
    return output_image1

def binary_morphology_open(image,kernal):
    image1=binary_morphology_erosion(image, kernal)
    output=binary_morphology_dilation(image1, kernal)
    return output

def binary_morphology_close(image,kernal):
    image1=binary_morphology_dilation(image, kernal)
    output=binary_morphology_erosion(image1, kernal)
    return output

def binary_morphology_distance(Image,Kernal):
    # gradation_list=list()

    old_image=Image
    output_matrix=np.zeros([Image.shape[0],Image.shape[1]])
    skeleton_matrix = np.zeros([Image.shape[0], Image.shape[1]])
    skeleton_matrix_slice=np.zeros([Image.shape[0], Image.shape[1],1000])
    skeleton_reconstruction_matrix=np.zeros([Image.shape[0], Image.shape[1],1000])
    distance_matrix_slice=np.zeros([Image.shape[0], Image.shape[1],1000])
    ITERATION=0
    while True:
        temp_image=binary_morphology_erosion(old_image,Kernal)
        temp_image1=np.zeros([Image.shape[0], Image.shape[0]])
        temp_row=Image.shape[0]-temp_image.shape[0]
        temp_column=Image.shape[1]-temp_image.shape[1]
        temp_image1[int(temp_row/2):int(temp_row/2)+temp_image.shape[0],int(temp_column/2):int(temp_column/2)+temp_image.shape[1]]=temp_image

        # temp_image[0,:]=0
        # temp_image[:,0]=0

        # temp_image[2:Image.shape[0], 2:Image.shape[0]] = temp_image[0:Image.shape[0] - 2, 0:Image.shape[0] - 2]
        # temp_image[0:2, :] = 0
        # temp_image[:, 0:2] = 0
        output_matrix=output_matrix+(old_image-temp_image1)*ITERATION
        distance_matrix_slice[:,:,ITERATION]=output_matrix
        skeleton_reconstruction_matrix[:,:,ITERATION]=temp_image1 - binary_morphology_open(temp_image1, Kernal)
        skeleton_matrix=skeleton_matrix+temp_image1-binary_morphology_open(temp_image1,Kernal)
        skeleton_matrix_slice[:,:,ITERATION]=skeleton_matrix

        # print("temp_image:",temp_image)
        # print("old_image:", old_image)
        # print(ITERATION)


        if old_image.any()==0:
            break
        old_image = temp_image1

        ITERATION+=1
        # print(ITERATION)

    return (distance_matrix_slice[:,:,0:ITERATION+1]/np.max(distance_matrix_slice)*255).astype(np.uint8),skeleton_matrix_slice[:,:,0:ITERATION+1],skeleton_reconstruction_matrix[:,:,0:ITERATION+1]/255

def binary_morphology_skeleton_reconstruct(skeleton_reconstruction_matrix,kernal):
    output_matrix=np.zeros([skeleton_reconstruction_matrix.shape[0],skeleton_reconstruction_matrix.shape[1]])
    output_matrix_slice=np.zeros([skeleton_reconstruction_matrix.shape[0],skeleton_reconstruction_matrix.shape[1],skeleton_reconstruction_matrix.shape[2]])
    for i in range(skeleton_reconstruction_matrix.shape[2]):
        temp_image = skeleton_reconstruction_matrix[:, :, i]
        for j in range(i+1):
            temp_image=binary_morphology_dilation(temp_image,kernal)
            temp_row = temp_image.shape[0] - output_matrix.shape[0]
            temp_column = temp_image.shape[1] - output_matrix.shape[1]
        output_matrix=output_matrix+temp_image[int(temp_row/2):int(temp_row/2)+output_matrix.shape[0],int(temp_column/2):int(temp_column/2)+output_matrix.shape[1]]
        output_matrix_slice[:,:,i]=output_matrix
    index=np.nonzero(output_matrix_slice)
    output_matrix_slice[index]=255

    return output_matrix_slice#.astype(np.uint8)

def binary_morphology_open_reconstruct(binary_image,kernal):
    original_V = binary_image
    opened_M = binary_morphology_open(original_V, kernal)
    while 1:
        reconstructed_T = opened_M
        opened_M = binary_morphology_dilation(opened_M, kernal)
        temp_row = opened_M.shape[0] - original_V.shape[0]
        temp_column = opened_M.shape[1] - original_V.shape[1]
        opened_M = opened_M[int(temp_row / 2):int(temp_row / 2) + original_V.shape[0],
                   int(temp_column / 2):int(temp_column / 2) + original_V.shape[1]]
        opened_M = np.minimum(opened_M, original_V)
        same_pix = opened_M == reconstructed_T
        if same_pix.all():
            break
    return reconstructed_T

def binary_morphology_dilation_reconstruct(mask,seed,kernal):
    original_V = mask.copy()
    opened_M = seed.copy()
    while 1:
        reconstructed_T = opened_M
        opened_M = binary_morphology_dilation(opened_M, kernal)
        temp_row = opened_M.shape[0] - original_V.shape[0]
        temp_column = opened_M.shape[1] - original_V.shape[1]
        opened_M = opened_M[int(temp_row / 2):int(temp_row / 2) + original_V.shape[0],
                   int(temp_column / 2):int(temp_column / 2) + original_V.shape[1]]
        opened_M = np.minimum(opened_M, original_V)
        same_pix = opened_M == reconstructed_T
        if same_pix.all():
            break
    return reconstructed_T

def binary_morphology_erosion_reconstruct(mask,seed,kernal):
    original_V = mask.copy()
    opened_M = seed.copy()
    while 1:
        reconstructed_T = opened_M
        opened_M = binary_morphology_erosion(opened_M, kernal)
        temp_row = original_V.shape[0] - opened_M.shape[0]
        temp_column = original_V.shape[1] - opened_M.shape[1]
        opened_M_temp=np.zeros([original_V.shape[0],original_V.shape[1]])
        opened_M_temp[int(temp_row / 2):int(temp_row / 2) + opened_M.shape[0],int(temp_column / 2):int(temp_column / 2) + opened_M.shape[1]]=opened_M
        opened_M =opened_M_temp
        opened_M = np.maximum(opened_M, original_V)
        same_pix = opened_M == reconstructed_T
        if same_pix.all():
            break
    return reconstructed_T

if __name__ == "__main__":
    # test binary_morphology_reconstruct
    binary_image=np.array([[1,0,1,1,0],[0,1,0,1,1],[1,1,0,1,1],[1,1,0,1,1],[1,0,1,0,0]])
    # kernal=np.array([[1,1,1],[1,1,1],[1,1,1]])
    kernal = np.zeros([4,4])+1
    seed=np.array([[1,0,0,0,1],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,0,1,0,1]])
    reconstructed_image=binary_morphology_erosion_reconstruct(seed,binary_image,kernal)



    binary_image1=pl.imread("D:\\image_process\\019082910020\\019082910020\\Image\\lena512.bmp")
    # binary_image1=pl.imread("D:\\image_process\\019082910020\\019082910020\\Image\\threads_marker.jpg")
    # binary_image1=pl.imread("D:\\image_process\\019082910020\\019082910020\\Image\\circle.jpg")
    # binary_image1=pl.imread("D:\\image_process\\019082910020\\019082910020\\Image\\small_circle.png")
    # binary_image1=pl.imread("C:\\Users\\ThinkPad\\Desktop\\Snipaste2.bmp")
    # binary_image1=np.array([[1,0,1,1,0],[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,0,1,0,0]])
    binary_image=binary_image1.copy()

    # binary_image=binary_image.astype(np.int16)
    # if binary_image.ndim>2:
    #     binary_image = (binary_image[:, :, 0] * 30 + binary_image[:, :, 1] * 59 + binary_image[:, :, 2] * 11) / 100
    # binary_image=binary_image/np.max(binary_image)*255
    # binary_image=binary_image.astype(np.int16)

    # temp_nozeros=np.nonzero(binary_image)
    # binary_image[temp_nozeros]=1
    binary_image=entropy_binary_gray_image(binary_image)*255
    # pl.figure(1)
    # pl.imshow(binary_image,cmap='Greys_r')
    # pl.show()
    kernal=np.array([[0,1,0],[1,1,1],[0,1,0]])
    kernal=np.array([[1,1,1],[1,1,1],[1,1,1]])

    #ape Algorithm for binary reconstruction
    # size_kernal_for_ape=4
    # kernal=np.zeros([size_kernal_for_ape,size_kernal_for_ape])+1


    # dilation_binary_image= binary_morphology_dilation(binary_image, kernal)
    # erosion_binary_image= binary_morphology_erosion(binary_image, kernal)
    # opening_binary_image= binary_morphology_open(binary_image, kernal)
    # closing_binary_image= binary_morphology_close(binary_image, kernal)
    distance_output_matrix, distance_skeleton_matrix,distance_skeleton_reconstruction_matrix= binary_morphology_distance(binary_image, kernal)

    binary_skeleton_reconstruction_matrix=binary_morphology_skeleton_reconstruct(distance_skeleton_reconstruction_matrix,kernal)
    # pl.figure(1)
    # pl.imshow(binary_image,cmap='Greys_r')
    # pl.show()
    #
    # pl.figure(2)
    # pl.imshow(dilation_binary_image-1,cmap='Greys_r')
    # pl.show()
    #
    # pl.figure(3)
    # pl.imshow(erosion_binary_image,cmap='Greys_r')
    # pl.show()
    #
    # pl.figure(4)
    # pl.imshow(opening_binary_image,cmap='Greys_r')
    # pl.show()
    #
    # pl.figure(5)
    # pl.imshow(closing_binary_image,cmap='Greys_r')
    # pl.show()
    # pl.figure(6)
    # pl.imshow(distance_skeleton_matrix,cmap='Greys_r')
    # pl.figure(7)
    # pl.imshow(distance_output_matrix, cmap='Greys_r')
    # pl.figure(8)
    # pl.imshow(binary_skeleton_reconstruction_matrix, cmap='Greys_r')
    # pl.show()


    #ape Algorithm for binary reconstruction       binary_image kernal
    # original_V=binary_image
    # opened_M=binary_morphology_open(original_V,kernal)
    # pl.figure(3)
    # pl.imshow(opened_M,cmap='Greys_r')
    # while 1:
    #     reconstructed_T=opened_M
    #     opened_M=binary_morphology_dilation(opened_M,kernal)
    #     temp_row = opened_M.shape[0] - original_V.shape[0]
    #     temp_column = opened_M.shape[1] - original_V.shape[1]
    #     opened_M = opened_M[int(temp_row / 2):int(temp_row / 2) + original_V.shape[0],int(temp_column / 2):int(temp_column / 2) + original_V.shape[1]]
    #     opened_M=np.minimum(opened_M,original_V)
    #     same_pix=opened_M==reconstructed_T
    #     if same_pix.all():
    #         break
    #
    # pl.figure(1)
    # pl.imshow(original_V,cmap='Greys_r')
    #
    # pl.figure(2)
    # pl.imshow(reconstructed_T,cmap='Greys_r')
    # pl.show()


    #morphological edge detection use lena512.bmp
    # dilation_binary_image= binary_morphology_dilation(binary_image, kernal)
    # erosion_binary_image= binary_morphology_erosion(binary_image, kernal)
    #
    # temp_row = dilation_binary_image.shape[0] - erosion_binary_image.shape[0]
    # temp_column = dilation_binary_image.shape[1] - erosion_binary_image.shape[1]
    # edge_s=dilation_binary_image[int(temp_row / 2):int(temp_row / 2) + erosion_binary_image.shape[0],int(temp_column / 2):int(temp_column / 2) + erosion_binary_image.shape[1]]- erosion_binary_image
    #
    # temp_row = dilation_binary_image.shape[0] - binary_image.shape[0]
    # temp_column = dilation_binary_image.shape[1] - binary_image.shape[1]
    # edge_e=dilation_binary_image[int(temp_row / 2):int(temp_row / 2) + binary_image.shape[0],int(temp_column / 2):int(temp_column / 2) + binary_image.shape[1]]- binary_image
    #
    # temp_row = binary_image.shape[0] - erosion_binary_image.shape[0]
    # temp_column = binary_image.shape[1] - erosion_binary_image.shape[1]
    # edge_i=binary_image[int(temp_row / 2):int(temp_row / 2) + erosion_binary_image.shape[0],int(temp_column / 2):int(temp_column / 2) + erosion_binary_image.shape[1]]- erosion_binary_image
    #
    #
    # pl.figure(1)
    # pl.imshow(binary_image,cmap='Greys_r')
    #
    # pl.figure(2)
    # pl.imshow(edge_s,cmap='Greys_r')
    #
    # pl.figure(3)
    # pl.imshow(edge_e,cmap='Greys_r')
    #
    # pl.figure(4)
    # pl.imshow(edge_i,cmap='Greys_r')
    # pl.show()



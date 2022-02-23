import numpy as np
import pylab as pl
from binary_morphology_image import binary_morphology_dilation_reconstruct,binary_morphology_erosion_reconstruct
from skimage.morphology import disk
#kernal 必须为方阵
def morphology_krnal_flip(kernal):
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

def gray_morphology_dilation(image,kernal):
    matrix_dim3 = kernal.shape[0] * kernal.shape[1]
    matrix = np.zeros([image.shape[0] + kernal.shape[0] - 1, image.shape[1] + kernal.shape[1] - 1, matrix_dim3])
    dim3_index = 0
    for i in range(kernal.shape[0]):
        for j in range(kernal.shape[1]):
            matrix[i:i + image.shape[0], j:j + image.shape[1], dim3_index] = image + kernal[i, j]
            dim3_index += 1
    output_image = np.max(matrix, axis=2)
    return output_image

def gray_morphology_erosion(image,kernal):
    matrix_dim3 = kernal.shape[0] * kernal.shape[1]
    matrix1 = np.zeros([image.shape[0] + kernal.shape[0] - 1, image.shape[1] + kernal.shape[1] - 1, matrix_dim3])
    kernal_flip = morphology_krnal_flip(kernal)
    dim3_index = 0
    for i in range(kernal.shape[0]):
        for j in range(kernal.shape[1]):
            matrix1[i:i + image.shape[0], j:j + image.shape[1], dim3_index] = image - kernal_flip[i, j]
            dim3_index += 1
    output_image1 = np.min(matrix1[kernal.shape[1] - 1:-kernal.shape[1] + 1, kernal.shape[0] - 1:-kernal.shape[0] + 1, :], axis=2)
    return output_image1

def gray_morphology_open(image,kernal):
    image1=gray_morphology_erosion(image,kernal)
    output=gray_morphology_dilation(image1,kernal)
    return output

def gray_morphology_close(image,kernal):
    image1=gray_morphology_dilation(image,kernal)
    output=gray_morphology_erosion(image1,kernal)
    return output

def gray_morphology_open_reconstruct(gray_image,kernal):
    original_V = gray_image
    opened_M = gray_morphology_open(original_V, kernal)
    while 1:
        reconstructed_T = opened_M
        opened_M = gray_morphology_dilation(opened_M, kernal)
        temp_row = opened_M.shape[0] - original_V.shape[0]
        temp_column = opened_M.shape[1] - original_V.shape[1]
        opened_M = opened_M[int(temp_row / 2):int(temp_row / 2) + original_V.shape[0],
                   int(temp_column / 2):int(temp_column / 2) + original_V.shape[1]]
        opened_M = np.minimum(opened_M, original_V)
        same_pix = opened_M == reconstructed_T
        if same_pix.all():
            break
    return reconstructed_T

def gray_morphology_close_reconstruct(gray_image,kernal):
    original_V = gray_image
    closed_M = gray_morphology_close(original_V, kernal)
    while 1:
        reconstructed_T = closed_M
        closed_M = gray_morphology_erosion(closed_M, kernal)
        closed_M_temp=np.zeros([original_V.shape[0],original_V.shape[1]])
        temp_row = closed_M_temp.shape[0] - closed_M.shape[0]
        temp_column = closed_M_temp.shape[1] - closed_M.shape[1]
        # temp_row = closed_M.shape[0] - original_V.shape[0]
        # temp_column = closed_M.shape[1] - original_V.shape[1]
        closed_M_temp[int(temp_row / 2):int(temp_row / 2) + closed_M.shape[0],int(temp_column / 2):int(temp_column / 2) + closed_M.shape[1]]=closed_M
        # closed_M = closed_M[int(temp_row / 2):int(temp_row / 2) + original_V.shape[0],
        #            int(temp_column / 2):int(temp_column / 2) + original_V.shape[1]]
        closed_M = np.maximum(closed_M_temp, original_V)
        M_temp=closed_M[int(temp_row / 2):int(temp_row / 2) + closed_M.shape[0],int(temp_column / 2):int(temp_column / 2) + closed_M.shape[1]]
        T_temp=reconstructed_T[int(temp_row / 2):int(temp_row / 2) + closed_M.shape[0],int(temp_column / 2):int(temp_column / 2) + closed_M.shape[1]]
        # same_pix = closed_M == reconstructed_T
        same_pix = M_temp == T_temp
        if same_pix.all():
            break
    return reconstructed_T

def morphological_gradient_subtract(big_image,small_image):

    temp_row = big_image.shape[0] - small_image.shape[0]
    temp_column = big_image.shape[1] - small_image.shape[1]
    edge_s=big_image[int(temp_row / 2):int(temp_row / 2) + small_image.shape[0],int(temp_column / 2):int(temp_column / 2) + small_image.shape[1]]- small_image
    return edge_s/2
def morphological_OBR(gray_image,kernal):
    # kernal = np.zeros([5, 5]) + 1
    opened_M = gray_morphology_open(gray_image, kernal)
    seed = opened_M.copy()
    mask = gray_image.copy()
    image11 = np.zeros([gray_image.shape[0], gray_image.shape[1]])
    output=np.zeros([gray_image.shape[0], gray_image.shape[1],256])
    for i in range(0,256):
        temp_seed=np.zeros([seed.shape[0],seed.shape[1]])
        temp_mask=np.zeros([mask.shape[0],mask.shape[1]])
        temp_seed_index=np.where(seed>=i)
        if temp_seed_index[0].shape[0]==0:
            output[:, :, i] = image11
            continue
        temp_mask_index = np.where(mask>=i)
        if temp_mask_index[0].shape[0] == 0:
            output[:, :, i] = image11
            continue
        temp_seed[temp_seed_index]=1
        temp_mask[temp_mask_index]=1
        temp_reconstruct=binary_morphology_dilation_reconstruct(temp_mask,temp_seed,kernal)
        image11=image11+temp_reconstruct
        output[:,:,i]=image11
    return output

def morphological_CBR(gray_image,kernal):
    opened_M = gray_morphology_close(gray_image, kernal)
    seed = opened_M.copy()
    mask = gray_image.copy()
    image11 = np.zeros([gray_image.shape[0], gray_image.shape[1]])
    output = np.zeros([gray_image.shape[0], gray_image.shape[1], 256])
    for i in range(0, 256):
        temp_seed = np.zeros([seed.shape[0], seed.shape[1]])
        temp_mask = np.zeros([mask.shape[0], mask.shape[1]])
        temp_seed_index = np.where(seed >= i)
        if temp_seed_index[0].shape[0] == 0:
            output[:, :, i] = image11
            continue
        temp_mask_index = np.where(mask >= i)
        if temp_mask_index[0].shape[0] == 0:
            output[:, :, i] = image11
            continue
        temp_seed[temp_seed_index] = 1
        temp_mask[temp_mask_index] = 1
        temp_reconstruct = binary_morphology_erosion_reconstruct(temp_mask, temp_seed, kernal)
        # temp_reconstruct=np.multiply(temp_mask,temp_seed)
        # temp_reconstruct = temp_seed
        image11 = image11 + temp_reconstruct
        output[:,:,i]=image11
    return output

if __name__ == "__main__":

    # image = np.array([[0,2,2,2,1],[1,2,6,2,1],[0,6,7,2,1],[1,1,6,1,-100],[1,0,2,2,1]])
    # kernal=np.array([[0,3],[3,4]])
    #
    # dilation_image=gray_morphology_dilation(image,kernal)
    # erosion_image=gray_morphology_erosion(image,kernal)
    # open_image=gray_morphology_open(image, kernal)
    # close_image=gray_morphology_close(image,kernal)

    # matrix_dim3=kernal.shape[0]*kernal.shape[1]
    # matrix=np.zeros([image.shape[0]+kernal.shape[0]-1,image.shape[1]+kernal.shape[1]-1,matrix_dim3])
    # dim3_index=0
    # for i in range(kernal.shape[0]):
    #     for j in range(kernal.shape[1]):
    #         # coord_x=i-0
    #         # coord_y=j-(-1)
    #         matrix[i:i+image.shape[0],j:j+image.shape[1],dim3_index]=image+kernal[i,j]
    #         dim3_index+=1
    # output_image=np.max(matrix,axis=2)
    #
    #
    # dim3_index=0
    # matrix1=np.zeros([image.shape[0]+kernal.shape[0]-1,image.shape[1]+kernal.shape[1]-1,matrix_dim3])
    # kernal_flip=morphology_krnal_flip(kernal)
    # for i in range(kernal.shape[0]):
    #     for j in range(kernal.shape[1]):
    #         matrix1[i:i+image.shape[0],j:j+image.shape[1],dim3_index]=image-kernal_flip[i,j]
    #         dim3_index+=1
    # output_image1=np.min(matrix1[kernal.shape[1]-1:-kernal.shape[1]+1,kernal.shape[0]-1:-kernal.shape[0]+1,:],axis=2)

    gray_image1=pl.imread("D:\\image_process\\019082910020\\019082910020\\Image\\lena512.bmp")
    gray_image1=pl.imread("C:\\Users\\ThinkPad\\Desktop\\Snipaste8.bmp")
    # gray_image1=pl.imread("C:\\Users\\ThinkPad\\Desktop\\OBR_test (1).bmp")
    gray_image=gray_image1
    # binary_image1=pl.imread("D:\\image_process\\019082910020\\019082910020\\Image\\threads_marker.jpg")
    # binary_image1=np.array([[1,0,1,1,0],[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,0,1,0,0]])

    #bmp needn't it

    gray_image=gray_image1.copy()
    gray_image=gray_image.astype(np.int16)
    # image.flags.writeable = True
    if gray_image.ndim>2:
        gray_image = (gray_image[:, :, 0] * 30 + gray_image[:, :, 1] * 59 + gray_image[:, :, 2] * 11) / 100
    gray_image= gray_image / np.max(gray_image) * 255
    gray_image=gray_image.astype(np.int16)

    #bmp needn't it

    # pl.figure(1)
    # pl.imshow(gray_image, cmap='Greys_r')
    # pl.show()

    # temp_nozeros=np.nonzero(binary_image)
    # binary_image[temp_nozeros]=1

    kernal=np.array([[0,1,0],[1,1,1],[0,1,0]])
    kernal=np.zeros([5,5])+1
    kernal=np.zeros([20,20])+1
    #test four opertors, kernal=np.zeros([5,5])+1
    # dilation_binary_image= gray_morphology_dilation(gray_image, kernal)
    # erosion_binary_image= gray_morphology_erosion(gray_image, kernal)
    # opening_binary_image= gray_morphology_open(gray_image, kernal)
    # closing_binary_image= gray_morphology_close(gray_image, kernal)
    # pl.figure(1)
    # pl.imshow(gray_image,cmap='Greys_r')
    #
    #
    # pl.figure(2)
    # pl.imshow(dilation_binary_image,cmap='Greys_r')
    #
    #
    # pl.figure(3)
    # pl.imshow(erosion_binary_image,cmap='Greys_r')
    #
    #
    # pl.figure(4)
    # pl.imshow(opening_binary_image,cmap='Greys_r')
    #
    #
    # pl.figure(5)
    # pl.imshow(closing_binary_image,cmap='Greys_r')
    # pl.show()

    #morphological gradient kernal=np.zeros([5,5])+1

    # dilation_binary_image= gray_morphology_dilation(gray_image, kernal)
    # erosion_binary_image= gray_morphology_erosion(gray_image, kernal)
    # def morphological_gradient_subtract(big_image,small_image):
    #
    #     temp_row = big_image.shape[0] - small_image.shape[0]
    #     temp_column = big_image.shape[1] - small_image.shape[1]
    #     edge_s=big_image[int(temp_row / 2):int(temp_row / 2) + small_image.shape[0],int(temp_column / 2):int(temp_column / 2) + small_image.shape[1]]- small_image
    #     return edge_s/2
    #
    #
    # gradient_s=morphological_gradient_subtract(dilation_binary_image,erosion_binary_image)
    # gradient_e=morphological_gradient_subtract(dilation_binary_image,gray_image)
    # gradient_i=morphological_gradient_subtract(gray_image,erosion_binary_image)
    # pl.figure(1)
    # pl.imshow(gray_image,cmap='Greys_r')
    # pl.figure(2)
    # pl.imshow(gradient_s,cmap='Greys_r')
    # pl.figure(3)
    # pl.imshow(gradient_e,cmap='Greys_r')
    # pl.figure(4)
    # pl.imshow(gradient_i,cmap='Greys_r')
    # pl.show()

    #Morphological Smoothing

    # # morphological reconstruction kernal=np.zeros([20,20])+1
    # original_V=gray_image
    # opened_M=gray_morphology_close(original_V,kernal)
    # pl.figure(1)
    # pl.imshow(gray_image,cmap='Greys_r')
    # pl.figure(2)
    # pl.imshow(opened_M,cmap='Greys_r')
    # while 1:
    #     reconstructed_T=opened_M
    #     opened_M=gray_morphology_dilation(opened_M,kernal)
    #     opened_M = opened_M[int(temp_row / 2):int(temp_row / 2) + original_V.shape[0],int(temp_column / 2):int(temp_column / 2) + o
    #     temp_row = opened_M.shape[0] - original_V.shape[0]
    #     temp_column = opened_M.shape[1] - original_V.shape[1]riginal_V.shape[1]]
    #     opened_M=np.minimum(opened_M,original_V)
    #     same_pix=opened_M==reconstructed_T
    #     if same_pix.all():
    #         break
    #
    # pl.figure(3)
    # pl.imshow(reconstructed_T,cmap='Greys_r')
    #
    # pl.show()
# OCR OBR:kernal = np.zeros([5, 5]) + 1
#     kernal = np.zeros([5, 5]) + 1
    # kernal=disk(10)+100
    # marker=gray_morphology_close(gray_image, kernal)
    # image11=morphology.reconstruction(marker,gray_image,method='erosion')
    # pl.figure(1)
    # pl.imshow(gray_image,cmap='Greys_r')
    # pl.figure(2)
    # pl.imshow(image11,cmap='Greys_r')
    # pl.show()
    # # # marker=gray_morphology_open(gray_image, kernal)
    # image11=morphology.reconstruction(marker,gray_image,method='dilation')
    # opened_M=gray_morphology_open(gray_image,kernal)
    #
    # seed=opened_M.copy()
    # mask=gray_image.copy()
    # image11=np.zeros([gray_image.shape[0],gray_image.shape[1]])
    # for i in range(0,256):
    #     temp_seed=np.zeros([seed.shape[0],seed.shape[1]])
    #     temp_mask=np.zeros([mask.shape[0],mask.shape[1]])
    #     temp_seed_index=np.where(seed>=i)
    #     if temp_seed_index[0].shape[0]==0:
    #         continue
    #     temp_mask_index = np.where(mask>=i)
    #     if temp_mask_index[0].shape[0] == 0:
    #         continue
    #     temp_seed[temp_seed_index]=1
    #     temp_mask[temp_mask_index]=1
    #     temp_reconstruct=binary_morphology_dilation_reconstruct(temp_mask,temp_seed,kernal)
        # image11=image11+temp_reconstruct

    # for i in range(0,256,10):
    #     temp_seed=np.zeros([seed.shape[0],seed.shape[1]])
    #     temp_mask=np.zeros([mask.shape[0],mask.shape[1]])
    #     temp_seed_index=np.where(seed>=i)
    #     if temp_seed_index[0].shape[0]==0:
    #         continue
    #     temp_mask_index = np.where(mask>=i)
    #     if temp_mask_index[0].shape[0] == 0:
    #         continue
    #     temp_seed[temp_seed_index]=1
    #     temp_mask[temp_mask_index]=1
    #     temp_reconstruct=binary_morphology_erosion_reconstruct(temp_mask,temp_seed,kernal)
    #     # temp_reconstruct=np.multiply(temp_mask,temp_seed)
    #     # temp_reconstruct = temp_seed
    #     image11=image11+temp_reconstruct
    #
    #
    # image11=morphological_CBR(gray_image,kernal)

    # watershed
    kernal = np.zeros([3, 3]) + 1
    gray_image=np.array([[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]])
    h_min=np.min(gray_image)
    h_max=np.max(gray_image)
    min_index=np.where(gray_image==h_min)
    temp_min_binary_matrix=np.zeros([gray_image.shape[0],gray_image.shape[1]])
    temp_min_binary_matrix[min_index]=1
    while 1:
        temp_seed =np.zeros([gray_image.shape[0],gray_image.shape[1]])
        temp_seed[min_index[0][0],min_index[1][0]]
        connect_area=binary_morphology_dilation_reconstruct(temp_min_binary_matrix,temp_seed , kernal)






    pl.figure(1)
    pl.imshow(gray_image,cmap='Greys_r')
    # pl.figure(2)
    # pl.imshow(image11,cmap='Greys_r')
    # pl.figure(3)
    # pl.imshow(opened_M,cmap='Greys_r')
    pl.show()

    # gray_image=np.array([[1,0,1,1,0],[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,0,1,0,0]])
    # kernal=np.array([[1,1,1],[1,1,1],[1,1,1]])
    # image11=morphology.erosion(gray_image,kernal)
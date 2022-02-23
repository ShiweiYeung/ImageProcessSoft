import numpy as np
from scipy import ndimage
import pylab as pl
def Matrix_to_Set(matrix):
    N = matrix.shape[0]
    output = set()
    for i in range(N):
        for j in range(N):
            if matrix[i,j] == 1:
                # temp=tuple([i, j])
                output.add(tuple([i, j]))
    return output



def Coordinates_Tranlate(input_set,translation_vector):
    output_set=set()
    for point in input_set:
        # temp_tuple=tuple([point[0]+translation_vector[0],point[1]+translation_vector[1]])
        output_set.add(tuple([point[0]+translation_vector[0],point[1]+translation_vector[1]]))
    return output_set

def Set_to_Matrix(input_set,Size):
    output_matrix=np.zeros([Size, Size])
    for temp_set in input_set:
        output_matrix[temp_set[0], temp_set[1]]=1
    return output_matrix

def Dilation_Operation(image,kernal):
    output_set=set()
    kernal_size=kernal.shape[0]
    image_set=Matrix_to_Set(image)
    for i in range(kernal_size):
        for j in range(kernal_size):
            if kernal[i,j]==1:
                # temp_set = Coordinates_Tranlate(image_set, [i,j])
                output_set = output_set | Coordinates_Tranlate(image_set, [i,j])
    output_matrix=Set_to_Matrix(output_set,image.shape[0]+kernal_size-1)

    return output_matrix

def Erosion_Operation(image,kernal):
    # output_set = set()
    kernal_size = kernal.shape[0]
    image_set = Matrix_to_Set(image)
    # kernal_set=np.nonzero(kernal)
    # output_set=Coordinates_Tranlate(image_set,kernal[kernal_set[]])
    k=0
    for i in range(kernal_size):
        for j in range(kernal_size):
            if kernal[i,j]==1:
                if k==0:
                    k+=1
                    output_set=Coordinates_Tranlate(image_set,[-i,-j])
                else:
                    output_set=output_set & Coordinates_Tranlate(image_set,[-i,-j])
    output_matrix=Set_to_Matrix(output_set,image.shape[0])

    return output_matrix

def Opening_Operation(Image,Kernal):
    temp_image=Erosion_Operation(Image, Kernal)
    output=Dilation_Operation(temp_image, Kernal)
    x=Kernal.shape[0]-1
    y=Image.shape[0]-Kernal.shape[0]+1
    return output[0:Image.shape[0], 0:Image.shape[0]]
    # return output
    # return output[(Kernal.shape[0]-1):Kernal.shape[0]-1+Image.shape[0],(Kernal.shape[0]-1):Kernal.shape[0]-1+Image.shape[0]]

def Closing_Operation(Image,Kernal):
    temp_image=Dilation_Operation(Image, Kernal)
    output=Erosion_Operation(temp_image, Kernal)
    # return output
    # return output
    return output[0:Image.shape[0], 0:Image.shape[0]]
    # [(Kernal.shape[0]-1):Kernal.shape[0]-1+Image.shape[0],(Kernal.shape[0]-1):Kernal.shape[0]-1+Image.shape[0]]

def Complementary_Image(Image):
    return 1-Image


def Distance_Operation(Image,Kernal):
    # gradation_list=list()
    old_image=Image
    output_matrix=np.zeros([Image.shape[0],Image.shape[0]])
    skeleton_matrix = np.zeros([Image.shape[0], Image.shape[0]])
    ITERATION=1
    while True:
        temp_image=Erosion_Operation(old_image,Kernal)
        temp_image[1:Image.shape[0],1:Image.shape[0]]=temp_image[0:Image.shape[0]-1,0:Image.shape[0]-1]
        temp_image[0,:]=0
        temp_image[:,0]=0

        # temp_image[2:Image.shape[0], 2:Image.shape[0]] = temp_image[0:Image.shape[0] - 2, 0:Image.shape[0] - 2]
        # temp_image[0:2, :] = 0
        # temp_image[:, 0:2] = 0
        output_matrix=output_matrix+(old_image-temp_image)*ITERATION
        skeleton_matrix=skeleton_matrix+temp_image-Opening_Operation(temp_image,Kernal)

        # print("temp_image:",temp_image)
        # print("old_image:", old_image)
        # print(ITERATION)


        if old_image.any()==0:
            break
        old_image = temp_image

        ITERATION+=1
        # print(ITERATION)

    return output_matrix,skeleton_matrix

# def Skeleton_Operation(matrix):



# original_image=plt.imread("D:\\image_process\\019082910020\\019082910020\\Image\\threads_marker.jpg")
# image=pl.imread("D:\\image_process\\019082910020\\019082910020\\Image\\circle.jpg")
# image=pl.imread("D:\\image_process\\019082910020\\019082910020\\Image\\small_circle.png")
image1=pl.imread("D:\\image_process\\019082910020\\019082910020\\Image\\lena512.bmp")
image=image1.copy()
# image.flags.writeable = True
if image.ndim>2:
    image = (image[:, :, 0] * 30 + image[:, :, 1] * 59 + image[:, :, 2] * 11) / 100

temp_nozeros=np.nonzero(image)
image[temp_nozeros]=1


image=np.array([[1,0,1,1,0],[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,0,1,0,0]])
# iamge_set=image_to_set(original_image,[0,0])

# out=coordinates_tranlate(image.Set,[1,1])
kernal=np.array([[0,1,0],[1,1,1],[0,1,0]])

dilation_image= Dilation_Operation(image, kernal)
erosion_image= Erosion_Operation(image, kernal)
opening_image= Opening_Operation(image, kernal)
closing_image= Closing_Operation(image, kernal)
#
#
# cross_shape=np.array([[0,1,0],[1,1,1],[0,1,0]])
# square_shape=np.array([[1,1,1],[1,1,1],[1,1,1]])
# disc_shape=np.array([[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]])
#
# image_distance,image_skeleton= Distance_Operation(image, cross_shape)
image_circle_distance=ndimage.distance_transform_edt(image)

pl.figure(1)
pl.imshow(image,cmap='Greys_r')
# pl.figure(2)
# pl.imshow(image_skeleton,cmap='Greys_r')
# pl.figure(3)
# pl.imshow(image_distance,cmap='Greys_r')
pl.figure(4)
pl.imshow(image_circle_distance,cmap='Greys_r')
pl.show()

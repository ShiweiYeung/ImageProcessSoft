import numpy as np
# from matplotlib import pyplot as plt
import pylab as pl
#image 可以不是方阵，但kernal要求是方阵
def Kernal_Flip(kernal):
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

def Image_Convolution(image,kernal):
    kernal_flip=Kernal_Flip(kernal)
    kernal_row=kernal.shape[0]
    image_row=image.shape[0]
    image_column=image.shape[1]
    output=np.zeros([image_row-kernal_row+1,image_column-kernal_row+1])
    for i in range(image_row-kernal_row+1):
        for j in range(image_column-kernal_row+1):
            output[i,j]=np.sum(image[i:i+kernal_row,j:j+kernal_row]*kernal_flip)
    output_abs=np.abs(output)
    temp_output=output_abs/np.max(output_abs)*255
    output=temp_output.astype(np.int32)
    return output

def gauss_filter(kernel_size=3, sigma=1):
    max_idx = kernel_size // 2
    idx = np.linspace(-max_idx, max_idx, kernel_size)
    Y, X = np.meshgrid(idx, idx)
    gauss_filter = np.exp(-(X**2 + Y**2) / (2 * sigma**2))
    gauss_filter /= np.sum(np.sum(gauss_filter))
    return gauss_filter
def median_filter(kernel_size=3):
    return np.zeros([kernel_size,kernel_size])+1/kernel_size

def ture_median_filter(image,kernal_size=3):
    output=np.zeros([image.shape[0]-kernal_size+1,image.shape[1]-kernal_size+1])
    for i in range(image.shape[0]-kernal_size+1):
        for j in range(image.shape[1]-kernal_size+1):
            temp=image[i:i+kernal_size,j:j+kernal_size].reshape((kernal_size*kernal_size,1))
            output[i,j]=np.sort(temp,axis=None)[int(kernal_size*kernal_size/2)]
    return output


if __name__ == '__main__':
    # test_image=pl.imread("D:\\image_process\\019082910020\\019082910020\\Image\\lena512.bmp")
    test_image=np.array([[1,1,1,2,2],[2,2,2,3,3,],[1,2,3,4,5,],[5,4,3,2,1],[1,1,1,1,1]])
    # pl.figure(1)
    # pl.imshow(test_image,cmap='Greys_r')
    #
    # kernal=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    # roberts_operator_x=np.array([[-1,0],[0,1]])
    # roberts_operator_y = np.array([[0, -1], [1, 0]])
    # sobel_operator_x=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    # sobel_operator_y=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    # prewitt_operator_x=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
    # prewitt_operator_y=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    #
    # # kernal_flip= Kernal_Flip(kernal)
    # roberts_x_convolution=Image_Convolution(test_image,prewitt_operator_x)
    # roberts_y_convolution = Image_Convolution(test_image, prewitt_operator_y)
    #
    # gauss_kernel1 = gauss_filter(kernel_size=5, sigma=3)
    # gauss_kernel2 = gauss_filter(kernel_size=5, sigma=1)
    # median_kernal1=median_filter(kernel_size=5)
    # median_kernal2 = median_filter(kernel_size=3)
    # image1=Image_Convolution(test_image,median_kernal1)
    # image2 = Image_Convolution(test_image, median_kernal2)
    # image3= Image_Convolution(test_image, roberts_operator_x)
    # pl.figure(2)
    # pl.imshow(image1,cmap='Greys_r')
    # pl.figure(3)
    # pl.imshow(image3, cmap='Greys_r')
    # pl.show()
    image=ture_median_filter(test_image,kernal_size=3)
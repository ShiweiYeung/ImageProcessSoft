import numpy as np
import pylab as pl

def entropy_algorithm(image):
    N=image.shape[0]*image.shape[1]
    n=np.zeros([256])
    P=np.zeros([256])
    H=np.zeros([255])
    for i in range(256):
        temp_index=np.where(image==i)
        n[i]=temp_index[0].shape[0]
        P[i]=n[i]/N
    for temp_threshold in range(0,255):
        if np.sum(P[0:temp_threshold+1])==0:
            Hb = -10000
        else:
            temp_P=P[0:temp_threshold+1]/np.sum(P[0:temp_threshold+1])
            index_temp_P=np.nonzero(temp_P)
            Hb=-temp_P[index_temp_P].dot(np.log2(temp_P[index_temp_P]))
        if np.sum(P[temp_threshold+1:256])==0:
            Hw = -10000
        else:
            temp_W = P[temp_threshold+1:256]/ np.sum(P[temp_threshold+1:256])
            index_temp_W = np.nonzero(temp_W)
            Hw = -temp_W[index_temp_W].dot(np.log2(temp_W[index_temp_W]))
        H[temp_threshold]=Hb+Hw
    return np.argmax(H)

def entropy_binary_gray_image(image):
    output=image.copy()
    threshold=entropy_algorithm(image)
    inde1=np.where(image>threshold)
    inde0 = np.where(image <=threshold)
    output[inde1]=1
    output[inde0]=0
    return output

def OTSU_algorithm(image):
    N=image.shape[0]*image.shape[1]
    n=np.zeros([256])
    P=np.zeros([256])
    between_var=np.zeros([256])
    for i in range(256):
        temp_index=np.where(image==i)
        n[i]=temp_index[0].shape[0]
        P[i]=n[i]/N
    iP=np.arange(256)*P
    for threshold in range(256):
        if np.sum(P[0:threshold+1])==0 or np.sum(P[threshold+1:256])==0:
            between_var[threshold] = 0
            continue
        else:
            w1=np.sum(P[0:threshold+1])
            u1=np.sum(iP[0:threshold+1])/w1
            if threshold<255:
                w2=np.sum(P[threshold+1:256])
                u2 = np.sum(iP[threshold+1:256]) / w2
            else:
                w2=0
                u2=0
            vb=w1*w2*(u1-u2)**2
            between_var[threshold]=vb
    return np.argmax(between_var)

def OTSU_binary_gray_image(image):
    output=image.copy()
    threshold=OTSU_algorithm(image)
    inde1=np.where(image>threshold)
    inde0 = np.where(image <=threshold)
    output[inde1]=1
    output[inde0]=0
    return output
def threshold_binary_gray_image(image,threshold):
    output = image.copy()
    inde1 = np.where(image > threshold)
    inde0 = np.where(image <= threshold)
    output[inde1] = 255
    output[inde0] = 0
    return output
if __name__ == '__main__':
    gray_image=np.array([[1,10,1,1,0],[10,1,1,1,1],[1,10,11,11,10],[12,12,1,1,1],[10,10,10,13,13]])
    # gray_image=pl.imread("C:\\Users\\ThinkPad\\Desktop\\Snipaste1.bmp")
    gray_image=pl.imread("D:\\image_process\\lena512.bmp")
    # gray_image=gray_image.astype(np.int16)
    # if gray_image.ndim>2:
    #     gray_image = (gray_image[:, :, 0] * 30 + gray_image[:, :, 1] * 59 + gray_image[:, :, 2] * 11) / 100
    # gray_image=gray_image/np.max(gray_image)*255
    # gray_image=gray_image.astype(np.int)
    binary_threshold=OTSU_algorithm(gray_image)
    binary_image=OTSU_binary_gray_image(gray_image)
    pl.figure(1)
    pl.imshow(gray_image,cmap='Greys_r')
    pl.figure(2)
    pl.imshow(binary_image,cmap='Greys_r')
    pl.show()




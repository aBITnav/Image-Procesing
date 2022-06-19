import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("img/sample2.jpg",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
h,v=img.shape

def D(i,j):
    return ((i-h/2)**2+(j-v/2)**2)**0.5

img2=img.copy()
k=3
weight=[1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9]

for i in range(h-k):
    for j in range(v-k):
        s=0
        for x in range(k):
            for y in range(k):
                s+=img[i+x][j+y]*weight[x*k+y]
        img2[i+k//2][j+k//2]=s
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

f = np.fft.fft2(img2)
fshift = np.fft.fftshift(f)
spectrum = 0.05*np.log(np.abs(fshift))




img3=img.copy()

for i in range(h):
    for j in range(v):
        img3[i][j]=255-img2[i][j]
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)


rows, cols = img.shape
crow,ccol = rows//2 , cols//2
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.imshow(img_back, cmap = 'gray')

plt.imshow(spectrum, cmap = 'gray')


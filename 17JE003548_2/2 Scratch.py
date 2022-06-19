import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import copy
img=cv.imread('C:/Users/shara/OneDrive/Desktop/17je003262_2/sample2.png',0)
h,w=img.shape
ar=np.zeros(256,dtype = int)
for i in range(h):
    for j in range(w):
        ar[img[i][j]]+=1
for i in range(256):
    if i>0:
        ar[i]+=ar[i-1]
newval=np.zeros(256,dtype =int)
for i in range(256):
    newval[i]=((float)(ar[i]-ar[0])/(h*w-ar[0]))*255
newimg=copy.deepcopy(img)
for i in range(h):
    for j in range(w):
        newimg[i][j]=newval[img[i][j]]
cv.imshow('original',img)
cv.imshow('enhanced',newimg)
cv.waitKey(0)
cv.destroyAllWindows()
plt.title("originalhistogram") 
bins = np.histogram(img.flatten(),256,[0,256])
plt.hist(img.flatten(),256,[0,256], color = '0')
plt.xlim([0,256])
plt.show()
plt.title("enhancedhistogram") 
bins = np.histogram(newimg.flatten(),256,[0,256])
plt.hist(newimg.flatten(),256,[0,256], color = '0')
plt.xlim([0,256])
plt.show()
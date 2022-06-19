import numpy as np
import cv2
img=cv2.imread('sample3.png',0)
cv2.imshow('img',img)
res1=cv2.blur(img,(3,3))
res2=cv2.blur(img,(5,5))
res3=cv2.blur(img,(7,7))
res4=cv2.blur(img,(9,9))
res5=cv2.blur(img,(11,11))
cv2.imshow('img',res1)
cv2.waitKey(0)
cv2.imshow('img',res2)
cv2.waitKey(0)
cv2.imshow('img',res3)
cv2.waitKey(0)
cv2.imshow('img',res4)
cv2.waitKey(0)
cv2.imshow('img',res5)
cv2.waitKey(0)
median1 = cv2.medianBlur(img,3)
cv2.imshow('img',median1)
cv2.waitKey(0)
median2 = cv2.medianBlur(img,5)
cv2.imshow('img',median2)
cv2.waitKey(0)

def con_min(data, filter_size):    
    indexer = (int)(filter_size / 2)
    
    new_image = data.copy()
    
    nrow, ncol = data.shape
    
    for i in range(nrow):
        
        for j in range(ncol):
            l=255
            
            for k in range(i-indexer, i+indexer+1):
                
                for m in range(j-indexer, j+indexer+1):
                    
                    if (k > -1) and (k < nrow):
                        
                        if (m > -1) and (m < ncol):
                            
                            l=min(l,data[k,m])
            new_image[i,j]=l
    return new_image
def con_max(data, filter_size):    
    indexer = (int)(filter_size / 2)
    
    new_image = data.copy()
    
    nrow, ncol = data.shape
    
    for i in range(nrow):
        
        for j in range(ncol):
            l=0
            
            for k in range(i-indexer, i+indexer+1):
                
                for m in range(j-indexer, j+indexer+1):
                    
                    if (k > -1) and (k < nrow):
                        
                        if (m > -1) and (m < ncol):
                            
                            l=max(l,data[k,m])
            new_image[i,j]=l
    return new_image
s1=con_min(img,5)
cv2.imshow('img',s1)
s2=con_max(img,5)
cv2.waitKey(0)
cv2.imshow('img',s2)
cv2.waitKey(0)
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:38:23 2021

@author: Abhi
"""
import cv2
img=cv2.imread("sample3.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,v=img.shape


#############################################################################
img2=img
k=3

for i in range(h-k):
    for j in range(v-k):
        s=0
        for x in range(k):
            for y in range(k):
                s+=(img[i+x][j+y])/(k*k)
        avg=s
        img2[i][j]=avg
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#############################################################################
img2=img
k=5

for i in range(h-k):
    for j in range(v-k):
        s=0
        for x in range(k):
            for y in range(k):
                s+=(img[i+x][j+y])/(k*k)
        avg=s
        img2[i][j]=avg
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#############################################################################
img2=img
k=7

for i in range(h-k):
    for j in range(v-k):
        s=0
        for x in range(k):
            for y in range(k):
                s+=(img[i+x][j+y])/(k*k)
        avg=s
        img2[i][j]=avg
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#############################################################################
img2=img
k=9

for i in range(h-k):
    for j in range(v-k):
        s=0
        for x in range(k):
            for y in range(k):
                s+=(img[i+x][j+y])/(k*k)
        avg=s
        img2[i][j]=avg
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#############################################################################

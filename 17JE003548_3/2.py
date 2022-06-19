# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:38:23 2021

@author: Abhi
"""
import cv2
img=cv2.imread("img/sample2.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,v=img.shape


############################ MEAN ########################################
img2=img.copy()
mask=img.copy()
out1=img.copy()
out2=img.copy()
k=5

for i in range(h-k):#mean filter
    for j in range(v-k):
        s=0
        for x in range(k):
            for y in range(k):
                s+=(img[i+x][j+y])//(k*k)
        avg=s
        img2[i][j]=avg
        
for i in range(h):#mask
    for j in range(v):
        mask[i][j]=img[i][j]-img2[i][j]
        
        
for i in range(h):#first output
    for j in range(v):
        out1[i][j]+=0.75*mask[i][j]

for i in range(h):#second Output
    for j in range(v):
        out2[i][j]+=mask[i][j]
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("image",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("image",out1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("image",out2)
cv2.waitKey(0)
cv2.destroyAllWindows()


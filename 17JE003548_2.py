# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:02:48 2021

@author: Abhi
"""

import cv2
import statistics as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sci

img=cv2.imread("img/sample.png",0)
#img = cv2.equalizeHist(img)

h,v=img.shape

w=3 #from input
k=0.34
R=img.std()

img2=img.copy()

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(h-w):
    for j in range(v-w):
        arr=[]
        for x in range(w):
            for y in range(w):
                arr.append(img[i+x][j+y])
        arr=np.array(arr)
        m=arr.mean()
        sd=arr.std()
        t=m*(1+k*(sd/R-1))
        if img[i][j]<=t:
            img2[i+w//2][j+w//2]=0
        else:
            img2[i+w//2][j+w//2]=255
        
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

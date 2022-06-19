# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:38:23 2021

@author: Abhi
"""
import cv2
import statistics as st
img=cv2.imread("sample3.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,v=img.shape

## PLEASE RUN THEM INDIVIDUALLY ORESLE FILTERS IS GETTING OVERLAPPED ##

############################ MIN ########################################
img2=img
k=3

for i in range(h-k):
    for j in range(v-k):
        arr=[]
        for x in range(k):
            for y in range(k):
                arr.append(img[i+x][j+y])
        mn=min(arr)
        img2[i][j]=mn
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

############################## MAX #######################################
img2=img
k=3

for i in range(h-k):
    for j in range(v-k):
        arr=[]
        for x in range(k):
            for y in range(k):
                arr.append(img[i+x][j+y])
        mn=max(arr)
        img2[i][j]=mn
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

############################## MEDIAN #######################################
img2=img
k=3

for i in range(h-k):
    for j in range(v-k):
        arr=[]
        for x in range(k):
            for y in range(k):
                arr.append(img[i+x][j+y])
        median=st.median(arr)
        img2[i][j]=median
        

############################ weighted ########################################
img2=img
k=3
weight=[0,1,0,0,1,0,0,1,0]

for i in range(h-k):
    for j in range(v-k):
        s=0
        for x in range(k):
            for y in range(k):
                s+=img[i+x][j+y]*weight[x*k+y]
        img2[i][j]=s
        
cv2.imshow("image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
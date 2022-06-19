# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:43:09 2021

@author: Abhi
"""

import cv2
import numpy as np
img=cv2.imread("img/sample3.tif",0)
h,w=img.shape
ar=np.zeros(256,dtype = int)

for i in range(h):
    for j in range(w):
        ar[img[i][j]]+=1
        
a=[]
intensity=[]

for i in range(10,51,10):
    intensity.append(i)
    a.append(round(ar[i]/455.625))
    
n=len(a)
code=[""]*n


def shan(l,r,s,cur):
    if l==r:
        code[l]=cur
        return
    x=0
    i=l
    while i<r and x<=s:
        x+=a[i]
        i+=1
    t=s/2
    cur0=cur+"1"
    cur1=cur+"0"
    shan(l,i-1,t,cur0)
    shan(i,r,t,cur1)
    

shan(0,4,32,"")
code=code[::-1]

for i in range(n):
    print(intensity[i],a[i],code[i])
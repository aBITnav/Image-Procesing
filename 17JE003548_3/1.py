# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:38:23 2021

@author: Abhi
"""
import cv2
import statistics as st
img=cv2.imread("img/sample1.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,v=img.shape





############################ BW ########################################

def gray_to_bin(img,th):
    for i in range(h):
        for j in range(v):
            if img[i][j]>=th:
                img[i][j]=255
            else:
                img[i][j]=0
    return img

bwimg=img.copy()

bwimg=gray_to_bin(bwimg,170)
cv2.imshow("image",bwimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

############################## MAX Component and Rectangle #######################################

def com(img):
    mnr,mnc,mxr,mxc,mx=0,0,0,0,0
    for i in range(len(img)):
        for j in range(len(img[0])):
            c,p,q,r,s=0,10000,10000,0,0
            if img[i][j] == 255:
                dfs(img, i, j,c,p,q,r,s)
                if c>mx:
                    mx=c
                    mnr,mnc,mxr,mxc=p,q,r,s
    return mx,mnr,mnc,mxr,mxc

    
def dfs( img, i, j,c,p,q,r,s):
    if i<0 or j<0 or i>=len(img) or j>=len(img[0]) or img[i][j] != 255:
        return
    c+=1
    img[i][j] = 0
    p=min(p,i)
    q=min(q,j)
    r=max(r,i)
    s=max(s,j)
    dfs(img, i+1, j,c,p,q,r,s)
    dfs(img, i+1, j-1,c,p,q,r,s)
    dfs(img, i, j-1,c,p,q,r,s)
    dfs(img, i-1, j-1,c,p,q,r,s)
    dfs(img, i-1, j,c,p,q,r,s)
    dfs(img, i-1, j+1,c,p,q,r,s)
    dfs(img, i, j+1,c,p,q,r,s)
    dfs(img, i+1, j+1,c,p,q,r,s)

temp=bwimg.copy()
mx,mnr,mnc,mxr,mxc=com(temp)

for i in range(mnc,mxc+1):
    bwimg[mnr][i]=100
    bwimg[mxr][i]=100

cv2.imshow("image",bwimg)
cv2.waitKey(0)
cv2.destroyAllWindows()


############################ Median ########################################

k=3
for i in range(h-k):
    for j in range(v-k):
        arr=[]
        for x in range(k):
            for y in range(k):
                arr.append(img[i+x][j+y])
        median=st.median(arr)
        bwimg[i][j]=median
        
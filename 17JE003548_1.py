# -*- coding: utf-8 -*-


import cv2
import statistics as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sci



img=cv2.imread("img/sample.png",0)
h,w=img.shape


cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


hist = cv2.calcHist([img],[0],None,[256],[0,256]) 

hist=sci.gaussian_filter(hist,sigma=1.07621)

plt.plot(hist)

imgeq = cv2.equalizeHist(img)

cv2.imshow("image",imgeq)
cv2.waitKey(0)
cv2.destroyAllWindows()

gauss=cv2.GaussianBlur(imgeq,(1,9),1.0762)

cv2.imshow("image",gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()



N=3#input
local_max=[]
local_min=[]
M=[]

for i in range(N):
    mx=max(hist[i*(255//N):(i+1)*(255//N)])
    mn=min(hist[i*(255//N):(i+1)*(255//N)])
    local_max.append(mx)
    local_min.append(mn)

print(local_max)



newimg=img.copy()
for k in range(N):
    L=255//N
    ar=hist[k*L:(k+1)*(L)]
    rng=(local_max[i]-local_min[i]
    for i in range(L):
        if i>0:
            ar[i]+=ar[i-1]
    ar=np.zeros(256,dtype = int)
    newval=np.zeros(L,dtype =int)
    for i in range(L):
        newval[i]=((float)(ar[i]-ar[0])/(h*w-ar[0]))
    
    
    for i in range(h):
        for j in range(w):
            if img[i][j]>=k*L and img[i][j]<(k+1)*L:
                newimg[i][j]=newval[img[i][j]-k*L]
        

cv2.imshow("image",newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()     
        
    



cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized)


'''

hist = cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.plot(hist)'''


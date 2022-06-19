# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:43:37 2021

@author: Abhi
"""

img = [[0,0,5,4,5,7,5,0],
     [0,0,5,4,1,7,0,0],
     [0,0,5,4,1,7,1,0],
     [0,0,5,0,1,7,1,0],
     [2,3,2,0,1,2,1,0],
     [2,3,2,0,0,2,0,0],
     [2,3,1,0,0,2,0,0],
     [2,3,1,0,0,2,0,0]]

ans=[]

for j in range(8):
    f=1
    for i in range(1,8):
        if img[i][j]==img[i-1][j]:
            f+=1
        else:
            ans.append((img[i-1][j],f))
            f=1
        
    if(f>1):
        ans.append({img[7][j],f})
        

            
print(ans)
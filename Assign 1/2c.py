#m path

import cv2
img=cv2.imread("img/sample2.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,v=img.shape

x1=int(input("Enter Source x coordinate\n"))
y1=int(input("Enter Source y coordinate\n"))
x2=int(input("Enter Destination x coordinate\n"))
y2=int(input("Enter Destination y coordinate\n"))



def dfs(path, img, i, j):
    if i<0 or j<0 or i>=len(img) or j>=len(img[0]) or img[i][j] != 255:
        return
    img[i][j] = 100
    path.append([i,j])
    
    if i==x2 and j==y2:
        print(path)
        print("\n")
        return
    dfs(path,img, i+1, j)
    dfs(path,img, i+1, j-1)
    dfs(path,img, i, j-1)
    dfs(path,img, i-1, j-1)
    dfs(path,img, i-1, j)
    dfs(path,img, i-1, j+1)
    dfs(path,img, i, j+1)
    dfs(path,img, i+1, j+1)
    
    del path[-1]


path=[]
dfs(path,img,x1,y1)


if img[x2][y2]==100:
    print("Connected\n\n")
    
else:
    print("Not Connected")

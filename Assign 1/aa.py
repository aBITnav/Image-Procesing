import cv2
img=cv2.imread("img/sample3.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,v=img.shape
th=0.5*256

def split(img, out, r1, r2, c1, c2):
    if r1 > r2 or c1 > c2:
        return
    arr=[]
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            arr.append(img[i][j])
    if max(arr) - min(arr) <= th:
        for i in range(r1, r2 + 1):
            out[i][c1] = 0
            if c2 == -1 + img.shape[1]:
                out[i][c2] = 255
        for j in range(c1, c2 + 1):
            out[r1][j] = 0
            if r2 == -1 + img.shape[0]:
                out[r2][j] = 0
        return
    rmid = (r1 + r2) // 2
    cmid = (c1 + c2) // 2
    split(img, out, r1, rmid, c1, cmid)
    split(img, out, rmid + 1, r2, c1, cmid)
    split(img, out, r1, rmid, cmid + 1, c2)
    split(img, out, rmid + 1, r2, cmid + 1, c2)

out=img.copy()

split(img, out, 0, h - 1, 0, v - 1)

cv2.imshow("image",out)
cv2.waitKey(0)
cv2.destroyAllWindows()

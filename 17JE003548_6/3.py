import cv2
img=cv2.imread("img/sample3.png",0)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,v=img.shape

th=0.5*256
out=img.copy()

def seg(rl, rr, cl, cr):
    if rl > rr or cl > cr:
        return
    arr=[]
    for i in range(rl, rr + 1):
        for j in range(cl, cr + 1):
            arr.append(img[i][j])
    if max(arr) - min(arr) <= th:
        for i in range(rl, rr + 1):
            out[i][cl] = 255
            if cr == v-1:
                out[i][cr] = 255
        for j in range(cl, cr + 1):
            out[rl][j] = 255
            if rr == h-1:
                out[rr][j] = 0
        return
    rm=(rl + rr)//2
    cm=(cl + cr)//2
    seg(rl, rm, cl, cm)
    seg(rm + 1, rr, cl, cm)
    seg(rl, rm, cm + 1, cr)
    seg(rm + 1, rr, cm + 1, cr)

seg(0, h - 1, 0, v - 1)
cv2.imshow("image",out)
cv2.waitKey(0)
cv2.destroyAllWindows()

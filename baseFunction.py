import cv2
import  numpy as np


img = cv2.imread('bear.jpg')
if img is None:
    print('读取失败，请检查路径')

kernel = np.ones((5,5),np.uint8)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img,(5,5),3)
img_canny = cv2.Canny(img,100,100)
img_dilation = cv2.dilate(img_canny,kernel,iterations=1)
img_erode = cv2.erode(img_dilation,kernel,iterations=1)

img_resized = cv2.resize(img,(500,300))
img_cropped = img[50:250,200:400]

cv2.imshow('origin',img)

'''
cv2.imshow('gray',img_gray)
cv2.imshow('blur',img_blur)
cv2.imshow('canny',img_canny)
cv2.imshow('dilation',img_dilation)
cv2.imshow('erode',img_erode)
'''
cv2.imshow('resized',img_resized)
cv2.imshow('cropped',img_cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()


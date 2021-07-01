import cv2
import numpy as np

img = cv2.imread("poker.jpg")

width, height = 250, 350
# 获取扑克卡的四个顶点的坐标
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
# 生成图片的四个顶点坐标
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# 获得变换矩阵
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# 将变换矩阵应用在图片上
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)


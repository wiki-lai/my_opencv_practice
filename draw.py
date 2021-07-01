import cv2
import numpy as np

img = np.ones((512,256,3),np.uint8)

img[:] = (255,0,0)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)
cv2.rectangle(img,(0,0),(100,100),(0,255,0),cv2.FILLED)
cv2.circle(img,(100,150),60,(0,255,0),2)
cv2.putText(img,'i love reze',(0,300),cv2.FONT_HERSHEY_SIMPLEX,1.5,(138,43,226),2)

cv2.namedWindow('background')

cv2.imshow('background',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

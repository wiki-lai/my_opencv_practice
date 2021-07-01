import cv2

cap = cv2.VideoCapture(0)
cap.open(0)


while cap.isOpened():
    sucess,img = cap.read()
    img_edge = cv2.Canny(img,100,100)
    cv2.imshow('edgeDetect',img_edge)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break


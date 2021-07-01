import cv2

cap = cv2.VideoCapture(r'F:\testdata\reze.mkv')
if not cap.isOpened():
    print('读取失败，请检查摄像头或视频路径')

cap.set(3,720)
cap.set(4,720)


while True:
    sucess,img = cap.read()
    cv2.imshow('reze.mkv',img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

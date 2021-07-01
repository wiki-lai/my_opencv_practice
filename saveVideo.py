import  cv2

cap = cv2.VideoCapture(r'F:\testdata\reze.mkv')
if not cap.isOpened():
    print("摄像头初始化失败")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out_file = cv2.VideoWriter(r'F:\testdata\reze_flip.mp4',fourcc,25,(960,720))

while cap.isOpened():
    sucess,img = cap.read()
    img_flip = cv2.flip(img,1)
    out_file.write(img_flip)
    cv2.imshow('flip reze',img_flip)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

out_file.release()
cv2.destroyAllWindows()
cap.release()

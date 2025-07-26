import cv2

cv2.namedWindow("win",cv2.WINDOW_NORMAL)

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow("win",frame)
    key=cv2.waitKey(100)
    if key==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
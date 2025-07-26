import cv2
import numpy as np

cv2.namedWindow("win",cv2.WINDOW_NORMAL)
cv2.resizeWindow('win',600,400)


def mouse_call(event,x,y,flags,userdata):
    print(event,x,y,flags,userdata)
img=np.zeros((400,600,3),np.uint8)
cv2.setMouseCallback('win',mouse_call,"111")

while True:
    cv2.imshow('win',img)
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()

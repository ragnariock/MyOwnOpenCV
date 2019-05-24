import cv2
import numpy as np


img = np.zeros((500,500,3), np.uint8)

cv2.line(img, (0,0), (500,500), (255,0,0), 5)
cv2.rectangle(img, (384,0), (400,120), (0,255,0),3)
cv2.circle(img, (256,256),90,(100,50,50),-1)


cv2.imshow("test",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
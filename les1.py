import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('girl.jpg',0)
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.imwrite('girlsave.png',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()


# img = cv2.imread('girl.jpg',0)
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()
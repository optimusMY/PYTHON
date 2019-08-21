import numpy as np
import cv2

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
print(contours[0])

'''cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
 -1 is find all contours, if you specify an index then only contour[i] will be drawed
 for example Number of contours = 9 detected in this example
 you can specify 0 to 8 for contour index
 
 (0, 255, 0) is bgr color of contour for drawing
 3 is thickness of contour lines
 
 
'''
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.drawContours(imgray, contours, -1, (0, 255, 0), 3)

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()

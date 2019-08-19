import cv2
import numpy as np


'''HSV COLOR SPACE DEFINITIONS
    HUE : PIGMENT 0-360
   SATURATION : TONE(DOMINANCE) OF HUE
   VALUE : BASICALLY BRIGHTNESS OF HUE
'''

def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    frame = cv2.imread('smarties.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")   # LowerHue
    l_s = cv2.getTrackbarPos("LS", "Tracking")   # LowerSaturation
    l_v = cv2.getTrackbarPos("LV", "Tracking")   # LowerValue

    u_h = cv2.getTrackbarPos("UH", "Tracking")   # UpperHue
    u_s = cv2.getTrackbarPos("US", "Tracking")   # UpperSaturation
    u_v = cv2.getTrackbarPos("UV", "Tracking")   # UpperValue

    l_b = np.array([l_h, l_s, l_v])  # lowerBound l_b consists of lower hsv bound
    u_b = np.array([u_h, u_s, u_v])  # upperBound u_b consists of upper hsv bound

    '''cv2.inRange() WILL FILTER COLORS BETWEEN lowerBound l_b and upperbound u_b'''
    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("maskframe", mask)
    cv2.imshow("resultframe", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()

import cv2

img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

if k == 27:  # if ESC pressed
    cv2.destroyAllWindows()
elif k == ord('s'):  # if s pressed
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()


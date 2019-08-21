
'''
import cv2
import numpy as np
img = cv2.imread("lena.jpg")
lower1 = cv2.pyrDown(img)  # lower resolution from img
lower2 = cv2.pyrDown(lower1)  # lower resolution from lower1
higher1 = cv2.pyrUp(lower2)  # the same resolution with lower1 but detail information loosed
higher2 = cv2.pyrUp(img)  # higher resolution from img but more blurred because of interpolation

cv2.imshow("original image", img)
cv2.imshow("lower1 res image", lower1)
cv2.imshow("lower2 res image", lower2)
cv2.imshow("higher1 res image", higher1)
cv2.imshow("higher2 res image", higher2)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''


'''
import cv2
import numpy as np
img = cv2.imread("lena.jpg")
layer = img.copy()
gaussian_pyramid_list = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid_list.append(layer)
    cv2.imshow(str(i), layer)


cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''


import cv2
import numpy as np
img = cv2.imread("lena.jpg")
layer = img.copy()
gaussian_pyramid_list = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid_list.append(layer)
    cv2.imshow(str(i), layer)

'''LAPLACIAN PYRAMID
builtin fonksiyon olarak yoktur
pyrup ve pyrdown sadece gaussian pyramid için builtin fonksiyondur
Laplacian pyramid gaussiandan  elde edilmektedir,
Laplacian pyramiddeki bir level, bu levelin gaussian pyramid ve üst levele expand edilmiş gaussian pyramidi 
arasındaki farka eşittir. cv2.subtract() ile bu fark alınmaktadır


'''



layer = gaussian_pyramid_list[5]
#cv2.imshow('upper level Gaussian Pyramid', layer)
laplacian_pyramid_list = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i])
    laplacian = cv2.subtract(gaussian_pyramid_list[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)


cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




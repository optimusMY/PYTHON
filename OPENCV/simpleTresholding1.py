
import cv2 as cv
import numpy as np

img = cv.imread('gradient.png', 0)
'''
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
50 den kucuk degerde olan pixeller 0 yani tam siyah yapılır
50den buyuk degerde olan pixeller ise max value yani 255 yapılır(degistirilebilir)

_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
THRESH_BINARY_INV den dolayi yukardaki ornegin tersi davranir
yani 200den kucuk degerdeki pixelleri 1 yani beyaz(255 max val) yapar
200den buyuk degerdeki pixelleri 0 yani siyah yapar

_, th3 = cv.threshold(img, 100, 255, cv.THRESH_TRUNC)
burada ise THRESH_TRUNC dan dolayi 100 den kucuk degerdeki pixeller degismez
127 den buyuk degerdeki pixeller ise 100 olarak kalir
yani th3 e kadar deegismez ve th3 ten sonra th degeri olarak sabit kalir


_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
THRESH_TOZERO dan dolayı 127 den kucuk degerdeki pixelleri sıfır yani siyaha dondurur
127 den buyuk degerdeki pixeller ise aynı degerde kalır
yani th4 den sonrası aynı kalır ancak th4 den oncesi siyaha döner


_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
THRESH_TOZERO_INV dan dolayı 127 den kucuk degerdeki pixeller aynen kalır
127 den buyuk degerdeki pixeller ise sıfır olur yani siyaha doner
yani th5 den sonrası siyaha doner ancak th5den oncesi aynı kalır

'''
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 100, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)


cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)

cv.waitKey(0)
cv.destroyAllWindows()

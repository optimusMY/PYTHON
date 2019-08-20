import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

'''kernel = np.ones((5, 5), np.float32)/25
kernel: blocksize:5x5 , coeff :1/25= 0.04
-------------------------
0.04 0.04 0.04 0.04 0.04
0.04 0.04 0.04 0.04 0.04
0.04 0.04 0.04 0.04 0.04
0.04 0.04 0.04 0.04 0.04
0.04 0.04 0.04 0.04 0.04
-------------------------
filter2D homojen olarak tum neighborlar homojen ağırlıklı toplanırken
GaussianBlur gausian filterda ise weighted sum ile neighborlar toplanır (bkz gaussian kernel)


'''
kernel = np.ones((5, 5), np.float32)/25

dst = cv2.filter2D(img, -1, kernel)  # homogeneous filter: average with neighbors from kernel
blur = cv2.blur(img, (5, 5))
gblur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)  # effective for "salt and pepper noise" images
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)  # effective for smoothing with resulting sharp edges

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

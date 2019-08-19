'''

import numpy as np
import cv2

img = cv2.imread('messi5.jpg', -1)

print(img.shape)  # returns number of ( rows, columns, channels) as a tuple
print(img.size)   # returns total num of pixels on image
print(img.dtype)  # returns datatype of each pixel

b, g, r = cv2.split(img)

cv2.imshow("window blue", b)
cv2.waitKey(3000)
cv2.imshow("window green", g)
cv2.waitKey(3000)
cv2.imshow("window red", r)
cv2.waitKey(3000)

img = cv2.merge((b, g, r))
cv2.imshow("window merge", img)
cv2.waitKey(0)

cv2.destroyAllWindows()

'''





'''ROI  stands for REGION OF INTEREST
specific area which we interested on image

for example we will copy the yellow ball on elsewhere on image


import numpy as np
import cv2

img = cv2.imread('messi5.jpg', -1)

print(img.shape)  # returns number of ( rows, columns, channels) as a tuple
print(img.size)   # returns total num of pixels on image
print(img.dtype)  # returns datatype of each pixel

b, g, r = cv2.split(img)

img = cv2.merge((b, g, r))  #merging the splitted channels



ball = img[280:340, 330:390]  # ROI  is a rectangular area --> [x1:y1, x2:y2]    = [topleftX:topleftY, bottomrightX:bottomrightY]

img[273:333, 100:160] = ball  # copying ball (ROI) to  another place on img

cv2.imshow("window ", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''




'''RESIZE AND ADD FUNCTIONS
'''

import numpy as np
import cv2

img = cv2.imread('messi5.jpg', -1)
img2 = cv2.imread('lena.jpg', -1)

print(img.shape)  # returns number of ( rows, columns, channels) as a tuple
print(img.size)   # returns total num of pixels on image
print(img.dtype)  # returns datatype of each pixel

img = cv2.resize(img, (640, 480))
img2 = cv2.resize(img2, (640, 480))


'''
#with cv2.add(src1,src2) src1 and src2 will be added with same weight
resultImage = cv2.add(img, img2)  

with cv2.addWeighted(src1,alpha,src2,beta,gamma) src1 and src2 will be added with specified weights
resultImage = saturate(src1_i*alpha +src2_i*beta +gamma )   '''
resultImage = cv2.addWeighted(img, .7, img2, .3, 0)  # gamma will be like brightness 0 to 255(fullwhite)




cv2.imshow("window ", resultImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


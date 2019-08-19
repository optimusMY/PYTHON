import cv2 as cv
import numpy as np

'''ADAPTIVE TRESHOLD
simple tresholdda sabit belirli bir treshold değerine göre filtreleme yapılmaktaydı
resimlerde özellikle de videolarda ise değişik image bölgelerinde farklı aydınlık seviyeleri sözkonusu olabileceği için
adaptive Treshold metodu geliştirilmiştir.
Bu metodda ortalama değer yada gaussian dağılımı yaklaşımlarıyla treshold değeri belirlenip uygulanmaktadır

ADAPTIVE_THRESH_MEAN_C yaklaşımında
her(X,Y) pixelin etrafındaki blocksizeXblocksize çerçevesi içindeki komşu pixellerle 
olan ortalamasını alıp  ve C constant değerini bu ortalamadan çıkararak
treshold değeri belirler, böylece değişken aydınlık seviyelerine uyum sağlanır

ADAPTIVE_THRESH_GAUSSIAN_C
ortalama alma şeklini gaussian dağılımına göre ağırlıklandırılmış toplamlar alınması yaklaşımıyla yapılmaktadır
bulunan değerden C constant çıkarılarak treshold değeri elde edilir. Gaussian hesaplanırken Default Sigma(std deviation)
blocksizeXblocksize için kullanılmaktadır


  

'''


img = cv.imread('sudoku.png', 0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # simple tresholdda anlatıldığı gibi
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)  #blocksize 11,const c=2
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)  #blocksize 11,const c=2

cv.imshow("Image", img)
cv.imshow("THRESH_BINARY", th1)
cv.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)

cv.waitKey(0)
cv.destroyAllWindows()

'''import cv2

from processamento.ContaOvos import conta
import numpy as np
import math
'''
from processamento.ExtracaoDeCaracteristicas.mask import AplicarMascara as AM


import cv2
import numpy as np

am = AM()
img = cv2.imread('C:\\imagens\\lua.png')
img = cv2.GaussianBlur(img, (5, 5), 0)
cimg = am.desenharMascara(img)
cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,10,
                            param1=50,param2=12,minRadius=0,maxRadius=20)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
im = cv2.imread('C:\\imagens\\lua.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im_gauss = cv2.GaussianBlur(imgray, (5, 5), 0)
ret, thresh = cv2.threshold(im_gauss, 127, 255, 0)
# get contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours_area = []
# calculate area and filter into new array
for con in contours:
    area = cv2.contourArea(con)
    if 1000 < area < 10000:
        contours_area.append(con)

contours_cirles = []

# check if contour is of circular shape
for con in contours_area:
    perimeter = cv2.arcLength(con, True)
    area = cv2.contourArea(con)
    if perimeter == 0:
        break
    circularity = 4*math.pi*(area/(perimeter*perimeter))
    print (circularity)
    if 0.7 < circularity < 1.2:
        contours_cirles.append(con)

cv2.imshow('teste', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''























'''class t:
    def __init__(self):
        self.img = cv2.imread('C:\\imagens\\lua.png')
        #self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        self.img = cv2.GaussianBlur(self.img, (7, 7), -1)
        self.pd = ProDI().ExtrairCaracteristicas(self.img)
        i = conta(self.img)
        #ret,self.img  = cv2.threshold(self.img , 127, 255, cv2.THRESH_BINARY_INV)

      
        
        cv2.drawContours(self.img, i[0], -1, (255, 0, 0), 2)
        #o, img =self.pd.ExtrairCaracteristicas(imagem=self.img)
        cv2.imshow('teste', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    
t()'''
import pyqrcode
import png
from pyqrcode import QRCode
import cv2
import numpy as np
import matplotlib.pyplot as plt


s = "WRITE YOUR LINK HERE!!!!"

url = pyqrcode.create(s)

url.svg("myqr.svg", scale = 5)

url.png('myqr.png', scale = 5)

img = cv2.imread("myqr.png", 1)

cv2.imshow("my qr code", img)

k = cv2.waitKey(0) &0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("myqr.png", img)
    cv2.destroyAllWindows()

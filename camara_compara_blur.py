import cv2
import numpy as np
from pyzbar.pyzbar import decode
import os

# se guarda en variable el tamano total de la imagen
alto_img = 480
ancho_img = 640
cam = cv2.VideoCapture(0)

cam.set(3,ancho_img)
cam.set(4,alto_img)

#counts
blcount3 = 0
blcount7 = 0

def foto():
    global blcount3, blcount7
    ok, img = cam.read()
    if not ok:
        return False
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    zero = np.zeros((alto_img, ancho_img))
    norm = cv2.normalize(gray, zero, 0, 255, cv2.NORM_MINMAX)
    blur = cv2.GaussianBlur(norm,(3,3),0)
    blur7 = cv2.GaussianBlur(norm,(7,7),0)
    cv2.imshow('blur', blur)
    #cv2.imshow('bw', bw)
    cv2.waitKey(1)
    blcode = decode(blur)
    if blcode:
        blcount3= blcount3 + 1
#        print("blur", blcode[0])
    bl7 = decode(blur7)
    if bl7:
        blcount7 = blcount7 + 1
#        print("gray", graycode[0])
    if bl7 or blcode :
        os.system("clear")
        print("bl3: {}, bl7: {}".format(blcount3, blcount7))

    return True


if __name__ == '__main__':
    while(1):
        foto()

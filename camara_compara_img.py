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
imgcount = 0
graycount = 0
normcount = 0
blcount = 0
bwcount = 0

def foto():
    global imgcount, graycount, normcount, blcount, bwcount
    ok, img = cam.read()
    if not ok:
        return False
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    zero = np.zeros((alto_img, ancho_img))
    norm = cv2.normalize(gray, zero, 0, 255, cv2.NORM_MINMAX)
    blur = cv2.GaussianBlur(norm,(3,3),0)
    ret3, bw = cv2.threshold(blur,0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('blur', blur)
    #cv2.imshow('bw', bw)
    cv2.waitKey(1)
    imgcode = decode(img)
    if imgcode:
        imgcount = imgcount + 1
    graycode = decode(gray)
    if graycode:
        graycount = graycount + 1
#        print("gray", graycode[0])
    normcode = decode(norm)
    if normcode:
        normcount = normcount + 1
#        print("norm", normcode[0])
    blcode = decode(blur)
    if blcode:
        blcount = blcount + 1
#        print("blur", blcode[0])
    bwcode = decode(bw)
    if bwcode:
        bwcount = bwcount + 1
#        print("bw", bwcode[0])
    if imgcount or graycode or normcode or blcode or bwcode:
        os.system("clear")
        print("original: {}, gray: {}, norm: {}, blur: {}, bw: {}".format(imgcount, graycount, normcount, blcount, bwcount))
    return True


if __name__ == '__main__':
    while(1):
        foto()

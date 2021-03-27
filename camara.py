import cv2
import numpy as np
from pyzbar.pyzbar import decode

# se guarda en variable el tamano total de la imagen
alto_img = 480
ancho_img = 640
cam = cv2.VideoCapture(0)
cam.set(3,ancho_img)
cam.set(4,alto_img)

def foto():
    ok, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    zero = np.zeros((alto_img, ancho_img))
    norm = cv2.normalize(gray, zero, 0, 255, cv2.NORM_MINMAX)
    blur = cv2.GaussianBlur(norm,(5,5),0)
    ret3, bw = cv2.threshold(blur,0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('Binary', bw)
    cv2.waitKey(7)
    for qr in decode(bw):
        print(qr)

if __name__ == '__main__':
    while(1):
        foto()

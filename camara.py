import cv2
from pyzbar.pyzbar import decode

# se guarda en variable el tamano total de la imagen
alto_img = 480
ancho_img = 640
cam = cv2.VideoCapture(0)
cam.release()
cam = cv2.VideoCapture(0)
cam.set(3,ancho_img)
cam.set(4,alto_img)

def foto():
    ok, img = cam.read()
    if ok:
        for qr in decode(img):
            print(qr)
        cv2.imshow('Result', img)
        cv2.waitKey(1)

if __name__ == '__main__':
    while(1):
        foto()

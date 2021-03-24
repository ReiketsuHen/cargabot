import cv2
import numpy as np 
from pyzbar.pyzbar import decode

# se guarda en variable el tamaño total de la imagen
tam_im_tot = 300
img = cv2.imread('qrcargabot.png')
code = decode(img)
code = code[0]
# la informacióñ del qr nos sirve para tener la seguridad
# de estar siguiendo el qr correcto
print("Información del qr: ", code.data.decode('utf-8') )
# una vez que nos aseguramos que el qr es el correcto vemos las
# coordenadas del qr en la imagen obtenida, buscamos su ubicación 
# y su tamaño
# Al momento de tomar el qr con la camara conocemos el tamaño
# de la imagen por lo cual conoceremos su ubicación con respecto a la camara por ahora es una imagen de 300 por 300 pixeles.
# no nos interesa si está centrado o no a lo alto, solo a los lados.
print("Ubicación: {:.2f} % centrado a lo largo".format((code.rect.left+code.rect.width/2)*100/tam_im_tot))
# imprimimos el tamaño del qr, despues se pondrá un tamaño optimo para que el robot se aleje o acerque del qr.
print("Tamaño QR: {:.2f} % del total de la imagen".format(code.rect.width*100/tam_im_tot))



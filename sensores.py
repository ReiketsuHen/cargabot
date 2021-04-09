import RPi.GPIO as GPIO
import time

trig = 21
echo = 20
GPIO.setmode(BCM)
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

def distancia:
  GPIO.output(trig,FALSE)
  time.sleep(0.000005)
  GPIO.output(trig,TRUE)
  time.sleep(0.000005)    #aprox 5us
  GPIO.output(trig,FALSE)
  while GPIO.input(echo)==0:
    time_start = time.time()
  while GPIO.input(echo)==1:
    time_end = time.time()
  time_dif = time_end - time_start
  dis = (0.0343/2)*time_dif
  
  return dis

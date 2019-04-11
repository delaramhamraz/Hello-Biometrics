import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)


while true:

    #blue light
    
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(3, GPIO.LOW)
    time.sleep(1)

   #yellow light
   
    GPIO.output(5, GPIO.HIGH) 
    GPIO.output(5, GPIO.LOW)
    time.sleep(3)

   #white light 
   
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(7, GPIO.LOW)
    time.sleep(1)  
   
    #change again to blue 
    GPIO.output(3, GPIO.LOW)
    time.sleep(1)
    
GPIO.cleanup()

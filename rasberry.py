import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,GPIO.HIGH)
time.sleep(1)
GPIO.output(7,GPIO.LOW)
time.sleep(1)
GPIO.cleanup()

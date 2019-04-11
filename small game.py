import time
import random
import RPi.GPIO as GPIO

#we detect which pin has been set 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(1,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(12.GPIO.IN)

print ("Reactoin time game")
print("Python Project 8")

print ("")
print("")

#the lights will tur on 
GPIO.output(3,GPIO.HIGH)
GPIO.output(13,GPIO.HIGH)
time.sleep(2)

#it will wait for 2 seconds and after it will be turned off 
GPIO.output(3,GPIO.LOW)
GPIO.output(13, GPIO.LOW)

print("The green light will stay on for a random amount of time between 1 and 10 seconds")
print("It will then swap to the red light")
print("As soon as it changes hit the switch")
print("We start in 5 seconds")

#the program will wait for 5 seconds
time.sleep(5)

#the pin 3 is on 
GPIO.output(3,GPIO.HIGH)

# it will stay on sometime between 1 sec and 10 
r = random.randit(1,10)
time.sleep(r)

#the green light will be off 
GPIO.output(3,GPIO.LOW)
#the red light will be on 
GPIO.output(13,GPIO.HIGH)
start = time.time()

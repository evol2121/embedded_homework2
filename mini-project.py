import RPi.GPIO as GPIO
import pygame.mixer 
from time import sleep
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


TRIG = 23
ECHO = 24
BUTTON = 17
RED = 21
YELLOW = 20 
GREEN = 16

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

pygame.mixer.init(48000,-16,1,1024)

soundA = pygame.mixer.Sound("/home/pi/python_games/match0.wav")
soundChannelA = pygame.mixer.Channel(1)

count = 0

while True:
    inputValue = GPIO.input(BUTTON) 
    if(inputValue == 0):
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(YELLOW, GPIO.LOW)
        GPIO.output(GREEN, GPIO.LOW)
    while inputValue==1:
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
   
        while GPIO.input(ECHO)==0:
    	        pulse_start = time.time()
        
        while GPIO.input(ECHO)==1:
	        pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        print "Distance: ", distance, "cm"
        inputValue = GPIO.input(BUTTON)
        if(distance <= 5.0) :
            soundChannelA.play(soundA)
            GPIO.output(RED, GPIO.HIGH)
            GPIO.output(YELLOW, GPIO.LOW)
            GPIO.output(GREEN, GPIO.LOW)
        time.sleep(.01)
        if(distance <= 10.0 and distance > 5.0) :
            soundChannelA.play(soundA)
            GPIO.output(RED, GPIO.LOW)
            GPIO.output(YELLOW, GPIO.HIGH)
            GPIO.output(GREEN, GPIO.LOW)
            time.sleep(.1)
        if(distance <= 20.0 and distance > 10.0) :
            soundChannelA.play(soundA)
            GPIO.output(RED, GPIO.LOW)
            GPIO.output(YELLOW, GPIO.LOW)
            GPIO.output(GREEN, GPIO.HIGH)
            time.sleep(.3)
    
            

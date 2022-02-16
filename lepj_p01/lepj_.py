# -*- coding: utf-8 -*-
# ## ###############################################
#
# osblink8.py
# Blinks to leds on pins 21, 23, 27, 29, 31, 33, 35, 37 using Raspberry Pi
#
# Autor: Leyva Perez Jose Luis
# License: MIT
#
# ## ###############################################
# import modules
import RPi.GPIO as GPIO
import time

# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

# loop 20 times
for i in range(20):
    
    # flash output pins
    # Turn leds on
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(29, GPIO.HIGH)
    GPIO.output(31, GPIO.HIGH)
    GPIO.output(33, GPIO.HIGH)
    GPIO.output(35, GPIO.HIGH)
    GPIO.output(37, GPIO.HIGH)
    time.sleep(1) #Wait 1s
    # Turn leds off
    GPIO.output(21, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(29, GPIO.LOW)
    GPIO.output(31, GPIO.LOW)
    GPIO.output(33, GPIO.LOW)
    GPIO.output(35, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    time.sleep(1)#Wait 1s
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# osmarquee.py
# The leds of the row light up continuously in a marquee from left to right, on pins 21, 23, 27, 29, 31, 33, 35, 37 using Raspberry Pi
#
# Autor: Leyva Perez Jose Luis
# License: MIT
#
# ## ###############################################

# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
import time

# setup pins

GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)
# loop 5 times

leds = [21, 23, 27, 29, 31, 33, 35, 37]

for i in range(20):
#The leds of the row light up continuously in a marquee from left to right.
	for pin in leds:
		time.sleep(0.2)                 # Wait 200ms
		GPIO.output(pin, GPIO.HIGH) # Turn led on
		time.sleep(0.2)                 # Espera 200ms
		GPIO.output(pin, GPIO.LOW)  # Turn led off
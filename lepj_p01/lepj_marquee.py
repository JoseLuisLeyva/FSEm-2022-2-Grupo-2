#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# marquee.py
# The leds of the row light up continuously in a marquee from left to right, on pins 32,26,24,22,18,16,12,10 using Raspberry Pi
#
# Autor: Leyva Perez Jose Luis
# License: MIT
#
# ## ###############################################

# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Imports sleep functon
from time import sleep
# Initializes virtual board (comment out for hardware deploy)
import virtualboard

# Disable warnings
# GPIO.setwarnings(False)
# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BOARD)

# Set up pins no. 32,26,24,22,18,16,12 and 10 as output and default it to low
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)


leds = [10, 12, 16, 18, 22, 24, 26, 32]

while True: # Forever
#The leds of the row light up continuously in a marquee from left to right.
	for pin in leds:
		sleep(0.2)                 # Wait 200ms
		GPIO.output(pin, GPIO.HIGH) # Turn led on
		sleep(0.2)                 # Espera 200ms
		GPIO.output(pin, GPIO.LOW)  # Turn led off
		


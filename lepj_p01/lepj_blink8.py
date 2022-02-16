#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# blink8.py
# Blinks to leds on pins 32,26,24,22,18,16,12,10 using Raspberry Pi
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

# Set up pins no. 32,26,24,22,18,16,12,10 as output and default it to low
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)


# Blink the leds
while True: # Forever
	sleep(0.5)                 # Wait 500ms
	# Turn led on
	GPIO.output(32, GPIO.HIGH) 
	GPIO.output(26, GPIO.HIGH)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(22, GPIO.HIGH)
	GPIO.output(18, GPIO.HIGH)
	GPIO.output(16, GPIO.HIGH)
	GPIO.output(12, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)

	sleep(0.5)                 # Wait 500ms
	# Turn leds off
	GPIO.output(32, GPIO.LOW)  
	GPIO.output(26, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(22, GPIO.LOW)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(10, GPIO.LOW)


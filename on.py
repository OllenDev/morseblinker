#!/usr/bin/python

import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,True)
time.sleep(240)
GPIO.output(7,False)
GPIO.cleanup()

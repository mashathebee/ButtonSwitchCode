#!/usr/bin/env python

import gpiozero 
import signal

def on_button_press(): 
	print("Button was pressed")

def on_button_release(): 
	print("Button was released")


mybutton1 = gpiozero.Button(5) 
mybutton1.when_pressed = on_button_press 
mybutton1.when_released = on_button_release
signal.pause()
#!/usr/bin/env python

from w1thermsensor import W1ThermSensor
import paho.mqtt.publish as publish
import time

def getTempInC():
	tempsensor = W1ThermSensor()
	temp_in_c = tempsensor.get_temperature()
	return temp_in_c


temp = getTempInC()

while True:
	publish.single("sensors/home/temp/1", temp, hostname="localhost")
	time.sleep(5)



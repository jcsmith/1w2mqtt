#!/usr/bin/env python

#
#Copyright (c) 2015, Joshua Smith
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without 
#modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this 
#list of conditions and the following disclaimer.
#
#2. Redistributions in binary form must reproduce the above copyright notice, 
#this list of conditions and the following disclaimer in the documentation 
#and/or other materials provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
#FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
#DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
#OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

"""
1w2mqtt.py - Publish temperature readings from a 1 wire temperature sensor as an mqtt message.

Command Line Arguments:

-b --broker	Broker wihch 1w2mqtt should connect. 
-d --delay Delay between sensor readings. - Implemented.
-t --topic  Base topic which 1w2mqtt should publish messages.
-v --verbose  Verbose - Implemented - might add more messages.
"""

from w1thermsensor import W1ThermSensor
import argparse
import logging
import paho.mqtt.publish as publish
import time

#parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--broker", help="Broker to connect.", default="localhost")
parser.add_argument("-d", "--delay", help="Time to delay between sensor readings.", type=int, default=5)
parser.add_argument("-v", "--verbose", help="Enable Verbose output.", action="store_true")


args = parser.parse_args()

if args.verbose:
	logging.basicConfig(level=logging.DEBUG)

logging.debug("Additional Verbosity Enabled.")


while True:
	#get a list of sensors:
	sensors = W1ThermSensor.get_available_sensors()
	if args.verbose:
		print sensors

	for sensor in sensors:
		reading = sensor.get_temperature()
		logging.debug ("Sensor %s has temp %f at %f" % (sensor.id, reading,time.time()))


		try:
			publish.single("sensors/temperature/%s" % sensor.id, "%s %s" % (reading,time.time()), hostname=args.broker)
		
		except:
			print "Error connecting to %s" % args.broker

	time.sleep(args.delay)

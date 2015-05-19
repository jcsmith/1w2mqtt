# 1w2mqtt
python daemon to expose Dallas One Wire temperature sensor readings to an MQTT topic named sensors/temperature/$SENSORID

##Requirements
- w1thermsensor
- paho.mqtt.publish
- time

##Command Line Arguments

- -b --broker Broker which 1w2mqtt shold connect.
- -d --delay delay Delay between sensor readings.
- -t --topic Topic to which 1w2mqtt should publish messages.
- -v --verbose Enable Verbose Logging.

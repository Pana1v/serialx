# check this for a great simple input/output script:
# http://shallowsky.com/software/scripts/ardmonitor

import serial
import time

# reading data from Arduino
arduino = serial.Serial("COM4", 9600)

while True:
    arduino.readline()
    time.sleep(2)

# writing data to Arduino
import serial # if you have not already done so
arduino = serial.Serial('/dev/tty.usbserial', 9600)
time.sleep(2)
arduino.write('5')


# Arduino resets on serial connect, add time.sleep(2) before writing
# to disable this feature:
# http://arduino.cc/playground/Main/DisablingAutoResetOnSerialConnection
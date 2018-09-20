#turn Relay 1 and 2 off and keep the off
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [5, 6, 13, 19]

# loop through pins and set mode and state to 'high'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)

# main loop
try:
  GPIO.output(5, GPIO.HIGH)
  print "Relay 1 OFF"
  GPIO.output(6, GPIO.HIGH)
  print "Relay 2 OFF"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

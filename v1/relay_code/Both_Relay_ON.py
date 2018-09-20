#turn Relay 1 and 2 on and keep them on
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
  GPIO.output(5, GPIO.LOW)
  print "Relay 1 ON"
  GPIO.output(6, GPIO.LOW)
  print "Relay 2 ON"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

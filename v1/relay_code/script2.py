#Loop through relays and never stop
#Can Damage relay contocats after prolonged use

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers
pinList = [5, 6, 13, 19]

# loop through pins and set mode and state to 'high'
for i in pinList: 
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop
SleepTimeS = 0.2

# main loop
try:
  while True:

    for i in pinList:
      GPIO.output(i, GPIO.LOW)
      time.sleep(SleepTimeS);

    for i in pinList:
      GPIO.output(i, GPIO.HIGH)
      time.sleep(SleepTimeS);

    pinList.reverse()

# End program with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

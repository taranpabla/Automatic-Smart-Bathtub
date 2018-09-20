#Turn on all relays in sequential order, the close all relays
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pinList = [5, 6, 13, 19]

for i in pinList:
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

SleepTimeL = 0.2

# main loop
try:
  GPIO.output(5, GPIO.LOW)
  print "ONE"
  time.sleep(SleepTimeL);
  GPIO.output(6, GPIO.LOW)
  print "TWO"
  time.sleep(SleepTimeL);
  GPIO.output(13, GPIO.LOW)
  print "THREE"
  time.sleep(SleepTimeL);
  GPIO.output(19, GPIO.LOW)
  print "FOUR"
  time.sleep(SleepTimeL);
  GPIO.cleanup()
  print "Good bye!"

# End program with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

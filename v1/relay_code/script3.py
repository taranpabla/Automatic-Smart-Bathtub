#randomly turn relays on and off
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
SleepTimeL = 0.2

# main loop
try:
  GPIO.output(5, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(6, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(13, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(19, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(6, GPIO.HIGH)
  GPIO.output(19, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(5, GPIO.HIGH)
  GPIO.output(13, GPIO.HIGH)
  GPIO.output(6, GPIO.LOW)
  GPIO.output(19, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(5, GPIO.LOW)
  GPIO.output(13, GPIO.LOW)
  GPIO.output(6, GPIO.HIGH)
  GPIO.output(19, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(6, GPIO.LOW)
  GPIO.output(13, GPIO.LOW)
  time.sleep(SleepTimeL);

  GPIO.output(5, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(6, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(13, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.output(19, GPIO.HIGH)
  time.sleep(SleepTimeL);

  GPIO.cleanup()
  print "Good bye!"

# End program with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

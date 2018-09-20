#Turn relay on and off 10 times than close program
#Display how many times the relay turned on and off
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers
pinList = [5]

# loop through pins and set mode and state to 'high'
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop
SleepTimeL = 0.2

# main loop
try:
   count = 9
   while (count > 0):

      print '   The count is:', count

      for i in pinList:
         GPIO.output(i, GPIO.LOW)
         time.sleep(SleepTimeL);

      pinList.reverse()

      for i in pinList:
         GPIO.output(i, GPIO.HIGH)
         time.sleep(SleepTimeL);

      pinList.reverse()
      count = count - 1


# End program with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

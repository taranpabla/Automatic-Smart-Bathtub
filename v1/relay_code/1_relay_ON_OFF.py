
#Change the value inside sleep() to change duration of realys being on
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
pinList = [5, 6, 13, 19]

for i in pinList:
    GPIO.setup(i, GPIO.OUT)

try:
    GPIO.output(5, GPIO.LOW) #lOW means the pump is on
    print "ON"
    sleep(5)
    GPIO.output(5, GPIO.HIGH)#HIGH means the pump is off
    print "OFF"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

GPIO.cleanup()# Reset GPIO settings to default

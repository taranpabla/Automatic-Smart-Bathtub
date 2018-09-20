import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
pinList = [5, 6, 13, 19]

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH) #Insures that the relay turn off before draining
 
try:
    run_time = float(input("How long would you like to run the pumps for during clean up "))

    print "Please prepare to drain Loop 1"
    sleep(5)

    GPIO.output(5, GPIO.LOW) #lOW means the pump is ON
    print "Please drain Loop 1"
    print "Relay 1 is now ON for " + str(run_time) + " seconds"

    sleep(run_time)

    GPIO.output(5, GPIO.HIGH) #HIGH means the pump is OFF
    print "Relay 1 is now OFF"

    print "Please prepare to drain Loop 2"
    sleep(5)

    GPIO.output(6, GPIO.LOW)
    print "Please drain Loop 2"
    print "Relay 2 is now ON for " + str(run_time) + " seconds"

    sleep(run_time)

    GPIO.output(6, GPIO.HIGH)
    print "Relay 2 is now OFF"

    print "Water has now drained both loops. Thank You"

# End program cleanly with keyboard. Can be used in case of emergency
except KeyboardInterrupt:
  print "  Quit"

GPIO.cleanup()# Reset GPIO settings to default on completation

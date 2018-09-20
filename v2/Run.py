#import all neccesary libaries for code to run
import RPi.GPIO as GPIO
from time import sleep
import math

def seconds_to_run():
    #This function calulates how long each pump has to run for to get a desired temp
    #Gets initial temp reading of water. Ask user for the temps and stores them in a float variable
    cold_water = float(input("What is the temp of the cold water in celsius "))
    hot_water = float(input("What is the temp of the hot water in celsius "))
    final_temp = float(input("What is the desired final temp of the water "))

    #Asks the user for the values of the container
    length = float(input("Give me the length in Centimeters, then press enter "))
    width = float(input("Give me the width in Centimeters, then press enter "))
    height = float(input("Give me the height in Centimeters, then press enter "))
    #Calculates the volume of container
    total_volume_cm = length * width * height
    total_volume_l = total_volume_cm/1000
    #Print the volume of container
    print ("Total volume = " + str(total_volume_l) + " liters")

    #Calculates the final volumes of water that are needed
    temp_change_hot = abs(float(final_temp - hot_water))
    temp_change_cold = abs(float(final_temp - cold_water))
    var1 = float(temp_change_cold / temp_change_hot)
    var2 = var1 + 1
    volume_cold = float(total_volume_l / var2)
    volume_hot = float(total_volume_l - volume_cold)

    #Initalize a constant varaibel for flow rate
    flow_rate = 4 #flow rate is 4 liters per 60 seconds

    #Declare seconds_cold and seconds_hot as global variable.
    #Calulate how long the pumps need to stay on for and assign them to the variables
    global seconds_cold
    seconds_cold = (volume_cold / flow_rate) * 60
    global seconds_hot
    seconds_hot = (volume_hot / flow_rate) * 60

    #Print all neccesary values
    print("Pump 1 will run for " + str(seconds_hot) + " seconds and deposit " + str(volume_hot) +" liters of hot water")
    print("Pump 2 will run for " + str(seconds_cold) + " seconds and deposit " + str(volume_cold) +" liters of cold water")

def run_pump(seconds_hot, seconds_cold):
    #This function actiavtes the pumps by controlling the GPIO pins
    #Set GPIO pins to BCM mode
    GPIO.setmode(GPIO.BCM)

    #Initalize the pins. Pin 5 is pump 1. Pin 6 is pump 2
    pinList = [5, 6]

    #set GPIO as a output
    for i in pinList:
        GPIO.setup(i, GPIO.OUT)

    #main loop for pumps
    try:
        #Pump 1 is hot water
        GPIO.output(5, GPIO.LOW) #lOW means the pump is on
        print "Pump 1 is on"
        sleep(seconds_hot)
        GPIO.output(5, GPIO.HIGH)#HIGH means the pump is off
        print "Pump 1 is off"

        #1 second delay between pumps turning on and off. This doen lot to overload the power supply
        sleep(1)

        #Pump 2 is cold water
        GPIO.output(6, GPIO.LOW) #lOW means the pump is on
        print "Pump 2 is on"
        sleep(seconds_cold)
        GPIO.output(6, GPIO.HIGH)#HIGH means the pump is off
        print "Pump 2 is off"

    # End program cleanly with keyboard. Can be used in case of energency
    except KeyboardInterrupt:
        print "  Quit"

    GPIO.cleanup()# Reset GPIO settings to default

def clean_up():
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


#Run second_to_run function. This will calulate the neccesary values to run pumps
seconds_to_run()
#Run run_pump fucntion. This uses the values from seconds_to_run to run pumps
run_pump(seconds_hot, seconds_cold)

print "Would you like to drain the loop"
clean_up_command = float(input("Type 1 for Yes or Type 2 for No  "))

if clean_up_command == 1:
    clean_up()
else:
    print "Thank You. Enjoy your bath"
    GPIO.cleanup()# Reset GPIO settings to default on completation

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
    print ("Total volume = " + str(total_volume_l) + " liters")#Print the volume of container

    #Calculates the final volumes of water that are needed
    temp_change_hot = abs(float(final_temp - hot_water))
    temp_change_cold = abs(float(final_temp - cold_water))
    var1 = float(temp_change_cold / temp_change_hot)
    var2 = var1 + 1
    volume_cold = float(total_volume_l / var2)
    volume_hot = float(total_volume_l - volume_cold)

    flow_rate = 4 #Initalize a constant varaible for flow rate. Flow rate is 4 liters per 60 seconds

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
    GPIO.setmode(GPIO.BCM)#Set GPIO pins to BCM mode
    pinList = [5, 6] #Initalize the pins

    for i in pinList:
        GPIO.setup(i, GPIO.OUT) #set GPIO as a output
    try:#main loop for pumps
        #Pump 1 is hot water
        GPIO.output(5, GPIO.LOW) #lOW means the pump is on
        print "Pump 1 is on"
        sleep(seconds_hot)
        GPIO.output(5, GPIO.HIGH)#HIGH means the pump is off
        print "Pump 1 is off"

        sleep(1)#1 second delay between pumps turning on and off. This doen lot to overload the power supply

        #Pump 2 is cold water
        GPIO.output(6, GPIO.LOW) #lOW means the pump is on
        print "Pump 2 is on"
        sleep(seconds_cold)
        GPIO.output(6, GPIO.HIGH)#HIGH means the pump is off
        print "Pump 2 is off"

    except KeyboardInterrupt: #End program cleanly with keyboard. Can be used in case of energency
        print "  Quit"
    GPIO.cleanup() #Reset GPIO settings to default

def clean_up():
    #This function draines the loop of all water
    GPIO.setmode(GPIO.BCM) #Set GPIO pins to BCM mode
    pinList = [5, 6, 13, 19] #Initalize the pins

    for i in pinList:
        GPIO.setup(i, GPIO.OUT) #set GPIO as a output
        GPIO.output(i, GPIO.HIGH) #Insures that the relay turn off before draining

    try:
        #Ask user how long they want to drain the pumps for
        run_time = float(input("How long would you like to run the pumps for during clean up "))

        #Drain Loop 1
        print "Please prepare to drain Loop 1"
        sleep(5)
        GPIO.output(5, GPIO.LOW) #lOW means the pump is ON
        print "Please drain Loop 1"
        print "Relay 1 is now ON for " + str(run_time) + " seconds"
        sleep(run_time)
        GPIO.output(5, GPIO.HIGH) #HIGH means the pump is OFF
        print "Relay 1 is now OFF"
        sleep(1)

        #Drain Loop 2
        print "Please prepare to drain Loop 2"
        sleep(5)
        GPIO.output(6, GPIO.LOW)
        print "Please drain Loop 2"
        print "Relay 2 is now ON for " + str(run_time) + " seconds"
        sleep(run_time)
        GPIO.output(6, GPIO.HIGH)
        print "Relay 2 is now OFF"

        print "Water has now drained both loops"
        print ""

        sleep(1)

        print"Testing all relays"
        sleep(1)
        GPIO.output(5, GPIO.LOW)
        print "Relay 1"
        sleep(0.3)
        GPIO.output(6, GPIO.LOW)
        print "Relay 2"
        sleep(0.3)
        GPIO.output(13, GPIO.LOW)
        print "Relay 3"
        sleep(0.3)
        GPIO.output(19, GPIO.LOW)
        print "Relay 4"
        sleep(0.3)
        GPIO.cleanup()
        print "Good bye!"

    except KeyboardInterrupt: #End program cleanly with keyboard. Can be used in case of energency
        print "  Quit"

seconds_to_run()#Run second_to_run function. This will calulate the neccesary values to run pump
print ""
run_pump(seconds_hot, seconds_cold)#Run run_pump fucntion. This uses the values from seconds_to_run to run pumps
print ""
print "Would you like to drain the loop" #Asks user if they want to drain loop
clean_up_command = float(input("Type 1 for Yes or Type 2 for No ")) #Stores user decison in variable
print ""
if clean_up_command == 1:#If user enters "1" the clean_up function is run
    clean_up()
else:
    print "Thank You. Enjoy your bath"#If the user types "2" the code will end

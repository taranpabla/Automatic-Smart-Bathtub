import math

#Gets initial temp reading of water. Ask user for the temps and stores them in a float variable
cold_water = float(input("What is the temp of the cold water in celsius "))
hot_water = float(input("What is the temp of the hot water in celsius "))
final_temp = float(input("What is the desired final temp of the water "))

#Calculates the volume of tub
#Asks the user for the values of the tub
length = float(input("Give me the length in Centimeters, then press enter "))
width = float(input("Give me the width in Centimeters, then press enter "))
height = float(input("Give me the height in Centimeters, then press enter "))
#Calculates the volume of container
total_volume_cm = length * width * height
total_volume_l = total_volume_cm/1000
print ("Total volume = ")
print(str(total_volume_l) + " liters")

#Calculates the final volumes of water that are needed
temp_change_hot = abs(float(final_temp - hot_water))
temp_change_cold = abs(float(final_temp - cold_water))
var1 = float(temp_change_cold / temp_change_hot)
var2 = var1 + 1
volume_cold = float(total_volume_l / var2)
volume_hot = float(total_volume_l - volume_cold)
print(str(volume_cold) +" liters of cold water are needed")
print(str(volume_hot) +" liters of hot water are needed")

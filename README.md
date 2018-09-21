# Automatic Smart Bathtub
## Link to Research Paper
https://tinyurl.com/bathtubproject



## Bill of Materials

* **Tub or Bucket**
* **Fitting, Clamps, Hose** 
    * *3/8in ID hose barb to 1/2in MIP (Connects hose to adapter)*
            * http://www.homedepot.com/p/Everbilt-Lead-Free-Brass-Pipe-Coupling-1-2-in-FIP-802209/300096268?keyword=747808
            * https://www.menards.com/main/plumbing/rough-plumbing/pipe-tubing-hoses-fittings-accessories/fittings/hose-barb-fittings/3-8-id-barb-x-1-2-mip-lead-free-brass-id-hose-barb-to-male-pipe-adapter/p-1444442671792.htm*
    * **1/2 FIP Coupling (Connects the adapter to sensor)**
        * http://www.homedepot.com/p/Everbilt-Lead-Free-Brass-Pipe-Coupling-1-2-in-FIP-802209/300096268?keyword=747808
    * **Hose Clamps**
        * http://www.homedepot.com/p/Everbilt-5-16-5-8-in-Stainless-Steel-Clamp-10-pack-626025E/202262868
    * **Tubing**
        * http://www.homedepot.com/p/Everbilt-1-2-in-O-D-x-3-8-in-I-D-x-20-ft-PVC-Clear-Vinyl-Tube-702294/207144235
* **Raspberry Pi 3**
    * _https://www.raspberrypi.org/magpi/raspberry-pi-3-specs-benchmarks/_ (https://www.raspberrypi.org/magpi/raspberry-pi-3-specs-benchmarks/)
* **Ardunio Uno R3 SMD**
    * https://www.arduino.cc/en/Main/ArduinoBoardUnoSMD
* **Breadboard**
    * https://www.adafruit.com/product/64
* **Assortment of Jumper Wires**
    * https://www.amazon.com/gp/product/B01EV70C78/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1
* **2 pin Connector for Pumps**
    * https://www.amazon.com/gp/product/B06WGN56V2/ref=oh_aui_detailpage_o00_s01?ie=UTF8&psc=1
* **3 Pin Connectors for flow rate sensor**
    * https://www.amazon.com/gp/product/B01AHJMR4A/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1
* **GPIO Breadboard Expansion Kit**
    * _https://www.adafruit.com/product/2028_ (https://www.adafruit.com/product/2028)
* **Pump**
    * https://www.amazon.com/gp/product/B01N75ZIXF/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1
* **Power Supply for Pump**
    * https://www.amazon.com/gp/product/B0111A8U9A/ref=oh_aui_detailpage_o07_s00?ie=UTF8&psc=1
* **4 Channel Relay**
    * _https://www.sainsmart.com/4-channel-5v-relay-module-for-pic-arm-avr-dsp-arduino-msp430-ttl-logic.html_ (https://www.sainsmart.com/4-channel-5v-relay-module-for-pic-arm-avr-dsp-arduino-msp430-ttl-logic.html)
* **Waterproof temp sensors**
    * https://www.adafruit.com/product/381
* **Flow Rate Sensor**
    * https://www.adafruit.com/product/828
* **4.7k ohm resistor for Temp Sensor**
    * https://www.amazon.com/gp/product/B0185FGYY2/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1
* **Pipe Cutter**
    * https://www.harborfreight.com/finger-release-ratcheting-pvc-cutter-62588.html


## Datasheets/Tutorials/Links/Notes

**Patent Link**
https://www.google.com/patents/US4563780

**Kind of similar example project**
https://www.youtube.com/watch?v=FNmN9hZslFI

**System that already exists**
https://www.moen.com/u

**Baby Bath Tub**
https://www.babylist.com/gp/4moms-infant-tub/2544/4175

**Math Code Using Thermodynamics**

* _https://www.quora.com/What-formula-can-I-use-to-calculate-how-much-hot-and-cold-water-to-add-in-order-to-hit-a-desired-target-volume-and-temperature_ (https://www.quora.com/What-formula-can-I-use-to-calculate-how-much-hot-and-cold-water-to-add-in-order-to-hit-a-desired-target-volume-and-temperature)
* _https://www.physicsforums.com/threads/volume-of-hot-cold-water-required-for-a-known-volume-and-temperature.616509/_ (https://www.physicsforums.com/threads/volume-of-hot-cold-water-required-for-a-known-volume-and-temperature.616509/)

## Software

* **Raspberry Pi NOOBS**
    * https://www.raspberrypi.org/downloads/noobs/
* **Arduino IDE**
    * https://www.arduino.cc/en/Main/Software
* **Fritzing**
    * http://fritzing.org/home/
        * http://omnigatherum.ca/wp/?p=87
        * http://omnigatherum.ca/wp/?p=338
        * https://github.com/adafruit/Fritzing-Library
            * https://learn.adafruit.com/using-the-adafruit-library-with-fritzing/import-the-library-into-fritzing
* **Atom Code viewer**
    * https://atom.io/

## Flow Rate sensor(Raspberry Pi)(Not working)

**Code**
https://learn.adafruit.com/adafruit-keg-bot/raspberry-pi-code
https://github.com/adafruit/Adafruit-Flow-Meter
https://github.com/adafruit/Kegomatic
https://github.com/attm2x/m2x-sample-cleverfaucet

**Questions/Tutorials**
https://raspberrypi.stackexchange.com/questions/62300/flow-meter-raspberry-circuit-and-problem-receiving-pulses
https://www.raspberrypi.org/forums/viewtopic.php?f=81&t=38208
_https://www.element14.com/community/community/raspberry-pi/blog/2013/04/16/tutorial-on-how-to-create-a-flowmeter-with-raspberry-pi-and-arduino-to-measure-water-used-in-gardening_ (https://www.element14.com/community/community/raspberry-pi/blog/2013/04/16/tutorial-on-how-to-create-a-flowmeter-with-raspberry-pi-and-arduino-to-measure-water-used-in-gardening)
_https://raspberrypi.stackexchange.com/questions/34480/how-to-use-the-water-flow-sensor-with-raspberry_ (https://raspberrypi.stackexchange.com/questions/34480/how-to-use-the-water-flow-sensor-with-raspberry)
_https://www.raspberrypi.org/forums/viewtopic.php?t=37924&p=411225_ (https://www.raspberrypi.org/forums/viewtopic.php?t=37924&p=411225)

**Videos**
https://www.youtube.com/watch?v=S8hOsEYz3Ow
https://www.youtube.com/watch?v=CtgP6Ewtinc
https://www.youtube.com/watch?v=ZMKwpaPl-Vk

## Flow Rate Sensor(Arduino**)(Working)

_Wiring_
Black = ground
yellow = Pin 2 (Data pin)
red = 5V

v1 code = http://www.bc-robotics.com/tutorials/using-a-flow-sensor-with-arduino/
*Code that was used: *v2 code = http://www.instructables.com/id/How-to-Use-Water-Flow-Sensor-Arduino-Tutorial/
https://diyhacking.com/arduino-flow-rate-sensor/

Code that hasn't been tested yet
_https://github.com/adafruit/Adafruit-Flow-Meter/blob/master/Adafruit_FlowMeter.pde_ (https://github.com/adafruit/Adafruit-Flow-Meter/blob/master/Adafruit_FlowMeter.pde)
_https://forum.arduino.cc/index.php?topic=8548.0_ (https://forum.arduino.cc/index.php?topic=8548.0)
_http://www.electroschematics.com/12145/working-with-water-flow-sensors-arduino/_ (http://www.electroschematics.com/12145/working-with-water-flow-sensors-arduino/)

https://www.youtube.com/watch?v=JLwpUv-fXZw
http://jume-maker.blogspot.com/2017/12/how-to-measure-liquid-volume-flow-rate.html 

## DS18B20 Temp sensor(Working)

_Wiring_
Black = ground = ground rail = Ground (Pin 9)
Yellow = data = GPIO4 (Pin 7)
Red = Voltage = 3.3V positive rail = 3V3 (Pin 1)

https://pimylifeup.com/raspberry-pi-temperature-sensor/
*Code that was used: *https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/software (https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20)

## Water Pump Control using Relay(Working)

_Relay Wiring_
GND = ground = ground rail = Ground (Pin 9)
IN1 = Relay 1/ Pump 1 = GPIO5 (Pin 29)
IN2 = Relay 2/ Pump 2 = GPIO6 (Pin 31)
IN3 = Relay 3 = GPIO 13 (Pin 33)
IN4 = Relay 4 = GPIO 19 (Pin 35)
VCC = 5V postive = 5V DC power (Pin 2)

*Code that was used:  *https://github.com/skiwithpete/relaypi/tree/master/4port
*4 Channel Relay Setup tutorial: *https://www.youtube.com/watch?v=OQyntQLazMU&feature=youtu.be
*Tutorial for wiring: *https://www.youtube.com/watch?v=xc1daIb1LVc

## Connect Arduino to raspberry pi

*Run the following commands in terminal to install the Arduino IDE*

sudo apt-get update
sudo apt-get install arduino
sudo reboot

Connect the Arduino to Raspberry Pi using usb cable
Run the Arduino IDE and open the serial monitor to read the flow rate rate in real time

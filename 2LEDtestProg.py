from machine import Pin as GPIO #Machine is Pico
from time import sleep
botLED = GPIO(15,GPIO.OUT)
topLED = GPIO("LED",GPIO.OUT)

try:
    while True:
        user_input = input("Which Light? 'Top', 'Bottom' or 'Both'?: ")
        if user_input == "Top" or user_input == "top":
            user2 = input("Flash or Steady?: ")
            if user2 == "Flash" or user2 == "flash":
                topLED.value(1) #VALUE
                sleep(0.1)
                topLED.value(0)
                sleep(0.1)
                topLED.value(1)
                sleep(.1)
                topLED.value(0)
            if user2 == "Steady" or user2 == "steady":
                topLED.value(1)
                sleep(4)
                topLED.value(0)
        if user_input == "Bottom" or user_input == "bottom":
            user2 = input("Flash or Steady?: ")
            if user2 == "Flash" or user2 == "flash":
                botLED.value(1) #VALUE
                sleep(0.1)
                botLED.value(0)
                sleep(0.1)
                botLED.value(1)
                sleep(.1)
                botLED.value(0)
            if user2 == "Steady" or user2 == "steady":
                botLED.value(1)
                sleep(4)
                botLED.value(0)
        if user_input == "Both" or user_input == "both":
            user2 = input("Flash or Steady?: ")
            if user2 == "Flash" or user2 == "flash":
                botLED.toggle(), topLED.toggle() #toggle mode ()
                sleep(0.1)
                botLED.toggle(), topLED.toggle() #toggle mode ()
                sleep(0.1)
                botLED.toggle(), topLED.toggle() #toggle mode ()
                sleep(.1)
                botLED.toggle(), topLED.toggle() #toggle mode ()
                sleep(.1)
                botLED.toggle(), topLED.toggle() #toggle mode ()
                sleep(.1)
                botLED.value(0), topLED.value(0)
            if user2 == "Steady" or user2 == "steady":
                botLED.value(1), topLED.value(1)
                sleep(4)
                botLED.value(0), topLED.value(0)
except KeyboardInterrupt:
    print("End")
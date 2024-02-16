Here's how to make your Pico on-board LED react using micro Python.
Onboard LED = topLED = GPIO("LED",GPIO.OUT)
-------------------------------------------------------------------------
I also added how to blink an extra Red LED (make sure to use a resistor!)
Red LED = botLED = GPIO(15,GPIO.OUT)
-------------------------------------------------------------------------
Please note: GPIO pins are interchangeable, set whichever pin you like.

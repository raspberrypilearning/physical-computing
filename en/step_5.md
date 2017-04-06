## Step 3: Switching an LED on and off

GPIO Zero is a new Python library which provides a simple interface to everyday GPIO components. It comes installed by default in Raspbian.

1. Open IDLE from the main menu (`Menu`>`Programming`>`Python 3 (IDLE)`.

1. You can switch an LED on and off by typing commands directly into the Python interpreter window (also known as the Python **shell**). Let's do this by first importing the GPIO Zero library. You also need to tell the Pi which GPIO pin you are using - in this case pin 17. Next to the chevrons `>>>`, type:

~~~ python
from gpiozero import LED
led = LED(17)
~~~

Press **Enter** on the keyboard.

1. To make the LED switch on, type the following and press **Enter**:

~~~ python
led.on()
~~~

1. To make it switch off you can type:

~~~ python
led.off()
~~~

1. Your LED should switch on and then off again. But that's not all you can do.

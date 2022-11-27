## Switching an LED on and off

GPIO Zero is a new Python library which provides a simple interface to everyday GPIO components. It comes installed by default in Raspbian.

+ Open Mu.

[[[mu-open]]]

+ You can switch an LED on and off by typing commands directly into the REPL. Click on the REPL button in the menu bar.

+ First import the GPIO Zero library, and tell the Pi which GPIO pin you are using - in this case pin 17.

    ``` python
    In [1]: from gpiozero import LED
    In [2]: led = LED(17)
    ```

    Press **Enter** on the keyboard.

+ To make the LED switch on, type the following and press **Enter**:

    ``` python
    In [3]: led.on()
    ```

+ To make it switch off you can type:

    ```python
    In [4]: led.off()
    ```

+ Your LED should switch on and then off again. But that's not all you can do.

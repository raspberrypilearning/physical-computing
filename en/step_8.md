## Step 6: Manually controlling the LED

You can now combine your two programs written so far to control the LED using the button.

1. Create a new file by clicking **File > New file**.

1. Save the new file by clicking **File > Save**. Save the file as `gpio_control.py`.

1. Now write the following code:

  ```python
  from gpiozero import LED, Button
  from time import sleep
  
  led = LED(17)
  button = Button(2)
  
  button.wait_for_press()
  led.on()
  sleep(3)
  led.off()
  ```
	
1. Save and run your program. When you push the button the LED should come on for three seconds.

## Step 5: Using buttons to get input

Now you're able to control an output component (an LED), let's connect and control an input component: a button. 

1. Connect a button to another GND pin and GPIO pin 2, like this:

    ![](images/button.png)

1. Create a new file by clicking **File > New file**.

1. Save the new file by clicking **File > Save**. Save the file as `gpio_button.py`.

1. This time you'll need the `Button` class, and to tell it that the button is on pin 2. Write the following code in your new file:

~~~ python
from gpiozero import Button
button = Button(2)
~~~

1. Now you can get your program to do something when the button is pushed. Add these lines:

~~~ python
button.wait_for_press()
print('You pushed me')
~~~

1. Save with **Ctrl + S** and run the code with **F5**. 
1. Press the button and your text will appear. 

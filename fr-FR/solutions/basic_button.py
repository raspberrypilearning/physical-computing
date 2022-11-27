from gpiozero import Button
button = Button(2) ##The pin the button is wired to

button.wait_for_press()
print('You pushed me')

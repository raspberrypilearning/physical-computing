from gpiozero import Motor
from time import sleep

motor1 = Motor(4, 14)
motor2 = Motor(17, 27)

motor1.forward()
motor2.forward()

while True:
    sleep(5)
    motor1.reverse()
    motor2.reverse()

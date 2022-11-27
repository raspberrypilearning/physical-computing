from gpiozero import Robot
from time import sleep

robot = Robot((4, 14), (17, 27))

robot.forward()
sleep(5)
robot.right()
sleep(1)
robot.backward()
sleep(1)
robot.left()
sleep(1)
robot.stop()

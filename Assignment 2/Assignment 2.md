Assignment 2 

Objective:

Make Romi32u4 move in a circle and square again, but this time using the raspberry pi, python, and a terminal on a host computer.



Procedure:

The square and circle code are conducted in a similar manner as assignment 1, but it utilizes the romipi_astar library instead to set twist targets. Additionally, we have to set up the Romi-RPI-i2cslave.ino to be uploaded to the rover to be able to receive commands from the raspberry pi. 

On a host computer, ssh onto the raspberry pi and run the CircleCode.py and SquareCode.py files through the python3 command.
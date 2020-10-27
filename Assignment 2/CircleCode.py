from romipi_astar.romipi_driver import AStar
import time

romi = AStar()
var = input("Enter any key to initiate circle: ") #Wait for user input
var = "a" #Illusion of choice back at it again
while var != "Q": #Stop condition of "Q"
	currentTime = time.time()
	nextTime = currentTime + 5.0 #Delay of 5s
	while currentTime < nextTime:
		romi.twist(0.25, 1.25)
		currentTime = time.time()
	romi.twist(0.0, 0.0)
	var = input("Enter any key to continue or press Q to stop: ")
from romipi_astar.romipi_driver import AStar
import time

romi = AStar()
var = input("Enter any key to initiate square: ") #Wait for user input
var = "a" #Illusion of choice back at it again
while var != "Q": #Stop condition of "Q"
    for i in range(4): #Loop 4 times
        currentTime = time.time() 
        nextTime = currentTime + 2.0
        while currentTime < nextTime: #Go forward for 2s  
            romi.twist(0.25, 0.0)
            currentTime = time.time()

        romi.twist(0.0, 0.0) #Stop
        currentTime = time.time()
        nextTime = currentTime + 1.1 #Twist for 1.1s
        while currentTime < nextTime:      
            romi.twist(0.0, 3.1415926/2)
            currentTime = time.time()
        romi.twist(0.0, 0.0) #Stop    
    var = input("Enter any key to continue or press Q to stop: ")
   
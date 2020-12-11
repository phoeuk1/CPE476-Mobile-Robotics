Assignment 1 



Objective:

Make the Romi32u4 move in a square and circle through the Arduino IDE



Procedure:

Using the Romi32u4.h library supplied by Pololu and the Arduino IDE, we can form basic shapes as paths for our rover.

For a square, the rover needs to move forward for a set duration, then turn 90 degrees and repeat that process 4 times total. To turn 90 degrees, set the speeds of the left and right wheels of the motor to a ratio and time how long it would take for an approximate 90 degrees to be met. During the straight forward motion, implement a for-loop to manage acceleration and deceleration.

For a circle, we repeat the process from the square for making a 90 degree turn, but we do it for a full 360 degree circle. 

As a finishing touch, the two codes have been set to be selected between a button A and button B located on the rover.




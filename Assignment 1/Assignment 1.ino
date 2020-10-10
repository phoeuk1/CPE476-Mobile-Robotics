#include <Romi32U4.h>

Romi32U4Motors motors;
Romi32U4ButtonA buttonA;
Romi32U4ButtonB buttonB;

void setup() 
{}

void loop() 
{
  bool clockwise = true;
  while (1)
  {
    if(buttonA.isPressed() == 1)
    {
      delay(2000);//Wait 2s before moving
      
      //Turn 4 times
      for(int i = 0; i < 4; i++)
      {
        //Accelerate forwards
        for(int speed = 150; speed < 300; speed++)
        { 
          motors.setSpeeds(speed-2,speed);
          delay(2);
        }
    
        delay(400); //Go straight for 2ms*300 + 400ms 
        
        //Slow and turn
        for(int speed = 300; speed > 130; speed--)
        {
          motors.setSpeeds(speed-2,speed);
          delay(2);
        }
        if(clockwise)motors.setRightSpeed(32);
        else motors.setLeftSpeed(0);
        delay(900);
      }
    }
  
    //Button B: Circular path
    else if(buttonB.isPressed() == 1)
    {
      delay(2000);
      if(clockwise) motors.setSpeeds(300,100);
      else motors.setSpeeds(100,300);
      delay(2100);   
    }
    
    //Stop
    motors.setSpeeds(0,0);
  }

}

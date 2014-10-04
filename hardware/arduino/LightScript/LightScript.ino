

/* Programming on a Teensy 2.0
 * I2C d -- SDA - pin 5
 * I2C c -- SCK - pin 6
 *
 */

/*
 *
 * BlinkM connections to Arduino
 * PWR - -- gnd -- black -- Gnd
 * PWR + -- +5V -- red   -- 5V
 * I2C d -- SDA -- green -- Analog In 4
 * I2C c -- SCK -- blue  -- Analog In 5
 *
 */

//  Created by Cesar Torres on 7/2/14.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#include "flixel.h"
#include <Wire.h>

#define BLINKM_FUNCS_DEBUG 1 

int script_id        = 16;   // 0 = programmable, 1-18 = ROM scripts
int script_reps      = 5;   // 0 = repeat infinitely
int script_fadespeed = 255;  // 1 = slowest fade, 255 = fastest fade
int script_timeadj   = 0;   // 0 = play back normally, + slower, - faster

int sensorValue; 
int sensorPin = A0;

int blinkmaddr = 0;            // 0 == broadcast, addresses all blinkms

Flixel f(blinkmaddr, script_id, script_reps, 
         script_fadespeed, script_timeadj);

void setup(){
    f.init();
}

char serInStr[30];
void loop(){
    if( readSerialString() ) {
        Serial.println(serInStr);
        char cmd = serInStr[0];
        int num = atoi(serInStr+1);
        if( cmd == 'W' ) {
            Serial.println("Writing new script...");
            
            Serial.println("done.");
        }
        else if( cmd == 'p' ) {
            Serial.println("Playing Script 0 repeatedly");
            f.play();
        }
        else if( cmd == 's'){
          sensorValue = analogRead(sensorPin);  
          float val = sensorValue / 1024.0;
          
          int speed = val * 50 - 25;
          Serial.println(speed);
          f.speed(speed);
        }
    }

}

/* Function: readSerialString
 * -
 * Read input from the Serial console. Note - baud rate = 19200
 * @global serInStr - input buffer
 */
/* Function: readSerialString
 * -
 * Read input from the Serial console. Note - baud rate = 19200
 * @global serInStr - input buffer
 */  

uint8_t readSerialString()
{
  if(!Serial.available()) {
    return 0;
  }
  delay(10);  
  int i = 0;
  while (Serial.available()) {
    serInStr[i] = Serial.read();   
    // FIXME: doesn't check buffer overrun
    i++;
  }
  serInStr[i] = 0;  
  return i; 
}

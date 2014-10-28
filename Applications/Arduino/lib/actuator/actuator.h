/*
 *  Actuator Interface - Header File
 *	------------------------------------
 *  Describes an actuator that receives one signal line (DC || PWM)
 *  An actuator is its own controller; outside controllers activate its behaviors. 
 *  For now, a behavior is defined as a sequence of integers [0, 1000]
 *  It regulates its own voltage thresholds
 */ 
#ifndef __Expresso__actuator__
#define __Expresso__actuator__

#include "string.h"
#include <Arduino.h>

class Actuator {
  public:
      Actuator(unsigned int, unsigned int, unsigned int) ;
      void init();
      void print();
      void set(Record*, uint16_t);
      void actuate(int);
      void go_to_pos(int);
      void next();
      void playable(boolean);
      void repeatable(boolean);
      boolean play;
      boolean repeat;

      inline uint16_t bound(boolean min){ 
        if(min) return vmin;
        else(max) return vmax;
      }

      inline length(){ return active_size;}
  private:
    Record* active_behavior;
    uint16_t active_size;
    uint8_t pin;
  
    uint16_t vmax;
    uint16_t vmin;
    uint16_t value;
    uint16_t pos;
};

#endif /* defined(__Expresso__actuator__) */

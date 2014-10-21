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
      void set(unsigned int*, unsigned int);
      void actuate(int);
      void go_to_pos(int);
      void next();
      void playable(boolean);
      void repeatable(boolean);
      boolean play;
      boolean repeat;

  private:
    unsigned int* active_behavior;
    unsigned int active_size;
    unsigned int pin;
  
    unsigned int vmax;
    unsigned int vmin;
    unsigned int value;
    int pos;
};

#endif /* defined(__Expresso__actuator__) */

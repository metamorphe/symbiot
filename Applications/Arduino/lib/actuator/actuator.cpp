/*
 *  Actuator Interface - Header File
 *	------------------------------------
 *  Describes an actuator that receives one signal line (DC || PWM)
 *  An actuator is its own controller; outside controllers activate its behaviors. 
 *  For now, a behavior is defined as a sequence of integers [0, 1000]
 *  It regulates its own voltage thresholds
 */ 
#include "actuator.h"

void Actuator::playable(boolean _play){ play = _play; }
void Actuator::repeatable(boolean _repeat){ repeat = _repeat;}

Actuator::Actuator(unsigned int _pin, unsigned int _vmin, unsigned int _vmax){
  pin = _pin;
  vmin = _vmin; // Arduino 0 --> always off load
  vmax = _vmax; // Arduino 255 --> always on load
  value = 0;
  pos = 0;
  play = false;
  repeat = true;
  Serial.print("Setup: " );
  Serial.print(vmin);
  Serial.print(" ");
  Serial.println(vmax);
  init();
} 

void Actuator::init(){
  pinMode(pin, OUTPUT);  
}

void Actuator::print(){
  Serial.print("Actuator ");
  Serial.print(": { value: ");
  Serial.print(value);
  Serial.println("}");
}

void Actuator::set(Record* _behavior, uint16_t size){
  playable(false);
  active_behavior = _behavior;
  active_size = size;
  go_to_pos(0);
}

void Actuator::actuate(int _value){
  value = map(_value, 0, 1000, vmin, vmax);
  analogWrite(pin, value);    
}


void  Actuator::go_to_pos(int _pos){ 
	if(_pos < 0) _pos = active_size + _pos; 
	pos = _pos;
}
// TODO: Add x # of repeats; currently inf. repeats
void Actuator::next(){
	if(!play) return;
	if(repeat && pos >= active_size){
		go_to_pos(0);
        } else if (!repeat && pos >= active_size) {
		playable(false);
		go_to_pos(0);
		return;
	}
	actuate(active_behavior[pos]->value);
	pos++;
}

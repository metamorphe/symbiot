//
//  Button.cpp
//  Buttons
//
//  Created by Cesar Torres on 7/2/14.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#include "Logger.h"

// A logger should be able to handle up to 65,535 samples
// Samples are normalized values from 0 to 256 (8bit-precision)

Logger::Logger(uint16_t _size, uint16_t _min, uint16_t _max){
  size = _size;
  state = READY;
  pos = 0;
  // Actuator bounds
  min_cap = _min; 
  max_cap = _max;
  init();
} 

void Logger::init(){
  clear();
}

void Logger::print(){
  Serial.print("Log ");
  Serial.print(": { size: ");
  Serial.print(size);
  Serial.println(", values: [");
  for(unsigned int i = 0; i < pos; i ++){
    Serial.print(_log[i].timestamp);
    Serial.print(":");
    Serial.print(_log[i].value);
    if(i != (pos - 1))
      Serial.print(", ");
  }
  Serial.println("]}");
  Serial.print("Elapsed time: ");
  Serial.println(last()->timestamp - first()->timestamp);
}

boolean Logger::clear(){
  pos = 0;
  state = READY;
  memset((void*)_log, 0, sizeof(_log));
  return true;
}
// logs normalized values
boolean Logger::log(uint16_t value){
  if(pos >= size){
    state = OUT_OF_MEMORY;
    return false;
  }
  Record r;
  r.value = value;
  r.timestamp = micros();
  _log[pos] = r;

  pos++;
  return true;
}
boolean Logger::write(char* filename){
}

boolean Logger::read(char* filename){
}

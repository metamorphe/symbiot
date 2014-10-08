//
//  Button.cpp
//  Buttons
//
//  Created by Cesar Torres on 7/2/14.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#include "logger.h"

Logger::Logger(){
  size = 20;
  max_cap = 1024;
  min_cap = 0;
  state = READY;
  pos = 0;
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
  for(unsigned int i = 0; i < size; i ++){
    Serial.print(_log[i]);
    if(i != (size - 1))
      Serial.print(", ");
  }
  Serial.println("]}");
}
boolean Logger::clear(){
  pos = 0;
  state = READY;
  memset((void*)_log, 0, sizeof(_log));
  return true;
}
// logs normalized values
boolean Logger::log(unsigned int value){
  if(pos >= size){
    state = OUT_OF_MEMORY;
    return false;
  }
  _log[pos] = value;
  pos++;
  return true;
}

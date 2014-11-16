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

  _log = (Record*) calloc(sizeof(Record*), _size);
  if (_log == NULL) Serial.println("OUT_OF_MEMORY - LOG ALLOC");
  init();
} 
Logger::Logger( const Logger& other ) :
   size( other.size ), max_cap( other.max_cap ), min_cap( other.min_cap )
  {
    state = READY;
    pos = 0;
    _log = (Record*) calloc(sizeof(Record*), size);
    if (_log == NULL) Serial.println("OUT_OF_MEMORY - LOG ALLOC");
    init();
  }

void Logger::init(){
  clear();
}

void Logger::printIR(){
  Serial.println("++++++++++ Schedule +++++++++++");
  Serial.println("----------------------------");
  Serial.println("|  curr  |  delay |  next  |");
  InterruptRecord ir;
  for(unsigned int i = 0; i < pos; i ++){
    ir = getIR(i);
    Serial.print("|  ");
    Serial.print(ir.curr);
    Serial.print("  |  ");
    Serial.print(ir.delay);    
    Serial.print("  |  ");
    Serial.print(ir.next);
    Serial.println("  |");
  }
  Serial.println("----------------------------");

  Serial.print("Elapsed time: ");
  double elapsed_time = ((double)(last()->timestamp) - (double)(first()->timestamp)) / 1000;
  Serial.print(elapsed_time);
  Serial.println("ms");
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
  double elapsed_time = ((double)(last()->timestamp) - (double)(first()->timestamp)) / 1000;
  Serial.print(elapsed_time);
  Serial.println("ms");
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
// logs normalized values
boolean Logger::log(uint16_t value, unsigned long timestamp){
  if(pos >= size){
    state = OUT_OF_MEMORY;
    return false;
  }
  Record r;
  r.value = value;
  r.timestamp = timestamp * 10000;
  _log[pos] = r;

  pos++;
  return true;
}


boolean Logger::read(char* filename){
  return true;
}

void Logger::write(String name, SDLogger& sd){
  String intensity = "";
  String timestr = "";
  String delimiter = "";


    // print to SD card internal log (CSV)
  Record* r;  
  for(uint8_t i = 0; i < length(); i++){
    r = get(i);

    intensity += delimiter;
    timestr += delimiter;
    intensity += r-> value;
    timestr += r-> timestamp;
    delimiter = ",";
  }
  sd.write(name, intensity);
  sd.write(name, timestr);
}

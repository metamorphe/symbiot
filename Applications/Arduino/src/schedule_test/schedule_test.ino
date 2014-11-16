#include <Arduino.h>
#include <SD.h>

#include "SDLogger.h"

SDLogger *s;
#define SCREEN_CSSD 4

// #define SCREEN_RST  0    
// #define SCREEN_DC   8
// #define SCREEN_CS  9
// #define SCREEN_CLK 13
// #define SCREEN_MOSI 11


void setup() {
  s = new SDLogger(SCREEN_CSSD);
  s->write(10);
}

void loop() {
  
}




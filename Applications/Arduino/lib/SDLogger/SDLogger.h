//
//  screen.h
//  Basic Screen Functionality
//
//  Created by Cesar Torres on 10/6/14.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __Expresso__sdlogger__
#define __Expresso__sdlogger__
#include <Arduino.h>
#include <SD.h>
#include "string.h"
// const int chipSelect = 4;

class SDLogger{
public:
    // CS
    SDLogger(uint8_t);
    void init();
    void write(String, String);
    void read();
    uint8_t open();
private:
  uint8_t cs; 
};

#endif /* defined(__Expresso__sdlogger__) */

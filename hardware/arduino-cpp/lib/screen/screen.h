//
//  screen.h
//  Basic Screen Functionality
//
//  Created by Cesar Torres on 10/6/14.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __Expresso__screen__
#define __Expresso__screen__

#include "string.h"
#include <Arduino.h>
#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library
#include <SPI.h>

#define FONT_COLOR 0x0000
#define BG_COLOR 0xffff

#if defined(__SAM3X8E__)
    #undef __FlashStringHelper::F(string_literal)
    #define F(string_literal) string_literal
#endif

class Screen{
public:
    Screen(uint8_t, uint8_t, uint8_t, uint8_t);
    void init();
    void clear();
    void println(int txt, uint8_t text_size = 1, uint16_t text_color = FONT_COLOR);
    void println(float txt, uint8_t text_size = 1, uint16_t text_color = FONT_COLOR);
    void println(char* txt, uint8_t text_size = 1, uint16_t text_color = FONT_COLOR);    
    void print(int txt, uint8_t text_size = 1, uint16_t text_color = FONT_COLOR);
    void print(float txt, uint8_t text_size = 1, uint16_t text_color = FONT_COLOR);
    void print(char* txt, uint8_t text_size = 1, uint16_t text_color = FONT_COLOR);
    int rgb(uint16_t r, uint16_t g, uint16_t b){
      return int(r/8*2048) + int(g/4*32)+ int(b/8);
    }
private:
    uint16_t time;
    uint16_t cursor_row;
    uint16_t cursor_col;
    uint8_t sdcs;
    void* tft;
};

#endif /* defined(__Expresso__screen__) */

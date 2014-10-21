/*
 *  Screen Interface - Header File
 *	------------------------------------
 *  Describes an TFT SPI Screen
 */ 


#include "screen.h"



Screen::Screen(uint8_t cs, uint8_t dc, uint8_t rst, uint8_t _sdcs){
  sdcs = _sdcs;
  time = millis();
  tft = (void*) new Adafruit_ST7735(cs, dc, rst);
  init();
} 

void Screen::init(){
  pinMode(sdcs, INPUT_PULLUP);  // don't touch the SD card
  ((Adafruit_ST7735*)tft)->initR(INITR_BLACKTAB);   // initialize a ST7735S chip, black tab
  clear();
  time = millis() - time;
}

void Screen::clear(){
  cursor_row = 0;
  cursor_col = 0;
  ((Adafruit_ST7735*)tft)->setCursor(cursor_row, cursor_col);
  ((Adafruit_ST7735*)tft)->setTextWrap(false);
  ((Adafruit_ST7735*)tft)->fillScreen(BG_COLOR);
}

void Screen::println(int txt, uint8_t text_size, uint16_t text_color){
  print(txt, text_size, text_color);
  ((Adafruit_ST7735*)tft)->println();
}
void Screen::println(float txt, uint8_t text_size, uint16_t text_color){
  print(txt, text_size, text_color);
  ((Adafruit_ST7735*)tft)->println();
}
void Screen::println(char* txt, uint8_t text_size, uint16_t text_color){
  print(txt, text_size, text_color);
  ((Adafruit_ST7735*)tft)->println();
}
void Screen::print(int txt, uint8_t text_size, uint16_t text_color){
  if(cursor_row > 19) clear();
  ((Adafruit_ST7735*)tft)->setTextWrap(true);
  ((Adafruit_ST7735*)tft)->setTextSize(text_size);  
  ((Adafruit_ST7735*)tft)->setTextColor(text_color);
  ((Adafruit_ST7735*)tft)->print(cursor_row);
  ((Adafruit_ST7735*)tft)->print(" ");
  ((Adafruit_ST7735*)tft)->print(txt);
  cursor_row ++;
}
void Screen::print(float txt, uint8_t text_size, uint16_t text_color){
  if(cursor_row > 19) clear();
  ((Adafruit_ST7735*)tft)->setTextWrap(true);
 ((Adafruit_ST7735*)tft)->setTextSize(text_size);
  ((Adafruit_ST7735*)tft)->setTextColor(text_color);
  ((Adafruit_ST7735*)tft)->print(cursor_row);
  ((Adafruit_ST7735*)tft)->print(" ");
  ((Adafruit_ST7735*)tft)->print(txt);
  cursor_row ++;
}
void Screen::print(char* txt, uint8_t text_size, uint16_t text_color){
  if(cursor_row > 19) clear();
  ((Adafruit_ST7735*)tft)->setTextWrap(true);
  ((Adafruit_ST7735*)tft)->setTextSize(text_size);  
  ((Adafruit_ST7735*)tft)->setTextColor(text_color);
  ((Adafruit_ST7735*)tft)->print(text_size);
  ((Adafruit_ST7735*)tft)->print(" ");
  ((Adafruit_ST7735*)tft)->print(txt);
  cursor_row ++;
}


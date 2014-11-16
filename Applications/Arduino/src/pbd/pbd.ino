#include <Arduino.h>
#include "Wire.h"

#include "Button.h"
#include "Logger.h"
#include "Sensor.h"
#include "Actuator.h"
#include "BlinkMActuator.h"
#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library
#include <SPI.h>

#if defined(__SAM3X8E__)
    #undef __FlashStringHelper::F(string_literal)
    #define F(string_literal) string_literal
#endif

#include "Screen.h"


#define RECORD_PIN 2
#define PLAYBACK_PIN 3
#define SENSOR_PIN A0
#define LED_PIN 13


Button *playback, *record;
Sensor *pot;
Logger *logger;
BlinkMActuator *led;
//Actuator *led;
Screen *s;

#define SCREEN_CS  10
#define SCREEN_DC   8
#define SCREEN_RST  0  
#define SCREEN_CSSD 5  


void setup() {
  Serial.begin(9600);

  Serial.println("Expresso");
  record = new Button("record", RECORD_PIN, NO_DEBOUNCE);
  playback = new Button("playback", PLAYBACK_PIN, NO_DEBOUNCE);
  pot = new Sensor(SENSOR_PIN, 0, 500);
 
  Serial.println("Setting up BlinkM");
  logger = new Logger(1000, 0, 100);
  led = new BlinkMActuator(0, 0, 100);
  led->init();
  Serial.println("Done setting up BlinkM");
  //  led = new Actuator(LED_PIN, 0, 255);
  s = new Screen(SCREEN_CS, SCREEN_DC, SCREEN_RST, SCREEN_CSSD);
  
  s->println("Expresso", 1);
}

void update(){
  record->read();
//  record->print();
  playback->read();
//  playback->print();
  pot->update();
  led->next();
  
  if(!led->play) {
    led->actuate(map(pot->value, 0, 1000, 0, 100));
//    Serial.println(map(pot->value, 0, 1000, 0, 100));  
  }
//  pot->print();
}
void logic(){
	if(playback->state == BUTTON_ENTER){
            if(led->play){ led->playable(false); }
            else{
                s->clear();
                Serial.println("Playback recording");
                s->println("Playback recording");
  		logger->print();
                led->set(logger->_log, logger->pos);
                led->playable(true);
            }
        }
       
       
        
	if(record->state == BUTTON_DOWN){
  		if(logger->state == OUT_OF_MEMORY){
  			Serial.println("Out of memory");
  			s->println("Out of memory");
  		} else{
  		    s->println((float) (pot->value));	
                    logger->log(pot->value);
  		}
  	} else if(record->state == BUTTON_ENTER){
  		logger->clear();
                led->playable(false);
                s->clear();
                Serial.println("Began recording");
                s->println("Began recording");
  		logger->log(pot->value);
                s->println((float) (pot->value));
  	} else if(record-> state == BUTTON_LEAVE){
           Serial.println("Stopped recording");  
           s->println("Stopped recording");  
        } 
}
void loop() {
  update();
  logic();
//  delay(30);
  
}




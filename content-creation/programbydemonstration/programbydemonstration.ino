#include "button.h"
#include "logger.h"
#include "sensor.h"
#include "actuator.h"

#define RECORD_PIN 2
#define PLAYBACK_PIN 3
#define SENSOR_PIN A0
#define LED_PIN 13


Button *playback, *record;
Sensor *pot;
Logger *logger;
Actuator *led;

void setup() {
  record = new Button("record", RECORD_PIN, NO_DEBOUNCE);
  playback = new Button("playback", PLAYBACK_PIN, NO_DEBOUNCE);
  logger = new Logger();
  led = new Actuator(LED_PIN, 0, 255);
  pot = new Sensor(SENSOR_PIN, 0, 500);
  Serial.begin(9600);
}

void update(){
  record->read();
//  record->print();
  playback->read();
//  playback->print();
  pot->update();
  led->next();
  if(!led->play) led->actuate(pot->value);
//  pot->print();
}
void logic(){
	if(playback->state == BUTTON_ENTER){
            if(led->play){ led->playable(false); }
            else{
                Serial.println("Playback recording");
  		logger->print();
                led->set((unsigned int*)logger->_log, logger->pos);
                led->playable(true);
            }
        }
       
       
        
	if(record->state == BUTTON_DOWN){
  		if(logger->state == OUT_OF_MEMORY){
  			Serial.println("Out of memory");
  		} else{
  			logger->log(pot->value);
  		}
  	} else if(record->state == BUTTON_ENTER){
  		logger->clear();
                led->playable(false);
                Serial.println("Began recording");
  		logger->log(pot->value);
  	} else if(record-> state == BUTTON_LEAVE){
           Serial.println("Stopped recording");  
        } 
}
void loop() {
  update();
  logic();
  delay(30);
  
}




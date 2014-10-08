#include "button.h"
#include "logger.h"
#include "sensor.h"

#define RECORD_PIN 2
#define PLAYBACK_PIN 3
#define SENSOR_PIN A0


Button *playback, *record;
Sensor *pot;
Logger *logger;

void setup() {
  record = new Button("record", RECORD_PIN, NO_DEBOUNCE);
  playback = new Button("playback", PLAYBACK_PIN, NO_DEBOUNCE);
  logger = new Logger();
  pot = new Sensor(SENSOR_PIN, 0, 500);
  Serial.begin(9600);
}

void update(){
  record->read();
//  record->print();
  playback->read();
//  playback->print();
  pot->update();
//  pot->print();
}
void logic(){

	if(playback->state == BUTTON_DOWN || playback->state == BUTTON_ENTER){
  		// playback the last log of values
  		logger->print();
                Serial.println("Stopped recording");
        }

	if(record->state == BUTTON_DOWN){
  		if(logger->state == OUT_OF_MEMORY){
  			Serial.println("Out of memory");
  		} else{
  			logger->log(pot->value);
  		}
  	} else if(record->state == BUTTON_ENTER){
  		logger->clear();
                Serial.println("Began recording");
  		logger->log(pot->value);
  	} else if(record-> state == BUTTON_LEAVE){
           Serial.println("Stopped recording");  
        } 
}
void loop() {
  update();
  logic();
  delay(1000);
  
}




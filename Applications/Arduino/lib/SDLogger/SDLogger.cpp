

#include "SDLogger.h"

// CS / MOSI / MISO / CLK

SDLogger::SDLogger(uint8_t _cs){
  cs = _cs;
  init();
} 

void SDLogger::init(){

  Serial.begin(9600);
  Serial.print("Initializing SD card...");
  pinMode(10, OUTPUT);
  if (!SD.begin(cs)) {
    Serial.println("Card failed, or not present");
    return;
  }
  Serial.println("card initialized.");
  
  char charBuf[50];
  String filename = "datalog.txt";
  filename.toCharArray(charBuf, 50);
  SD.remove(charBuf);

}

void SDLogger::write(String name, String value){
  
  char charBuf[name.length()];
  name.toCharArray(charBuf, name.length());

  File dataFile = SD.open(charBuf, FILE_WRITE);
  if (dataFile) {
    dataFile.println(value);
    dataFile.close();
    Serial.println(value);
  }  
  else {
    Serial.print("Error: Cannot open ");
    Serial.println(name);
  } 

}









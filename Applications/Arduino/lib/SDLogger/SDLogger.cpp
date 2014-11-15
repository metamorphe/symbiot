

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

  SD.remove("datalog.txt");

}

void SDLogger::write(int num){

  String dataString = "";
  dataString += String(num);

  
  
  File dataFile = SD.open("datalog.txt", FILE_WRITE);
  if (dataFile) {
    dataFile.println(dataString);
    dataFile.close();
    Serial.println(dataString);
  }  
  else {
    Serial.println("error opening datalog.txt");
  } 

}









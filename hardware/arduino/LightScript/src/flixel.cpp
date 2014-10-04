//
//  flixel.cpp
//  Flixels
//
//  Created by Cesar Torres on 7/2/14.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#include "flixel.h"

Flixel::Flixel(int _addr, int _script, int _reps, int _fadespeed, int _timeadj){
	addr = _addr;
	reps = _reps;
	fadespeed = _fadespeed;
	timeadj = _timeadj;
  script = _script;
  verbose(true);
} 

void Flixel::verbose(bool _v){ isVerbose = _v; }
void Flixel::speed(int s){ BlinkM_setSpeed(addr, s); }
bool Flixel::on(){
	print("Looking for BlinkM");
	BlinkM_beginWithPower();
        BlinkM_stopScript( addr );
        addr = BlinkM_findFirstI2CDevice();
        if( addr == -1 ) { print("No I2C devices found"); return false;}
        printp("Device found at addr ", addr);
        BlinkM_setAddress( addr );
        BlinkM_setSpeed(addr, -18);
        return true;
}
void Flixel::init(){
    Serial.begin(19200);
    print("BlinkMSetStartupScript");
   	if(! on()){ print("BlinkM not found. :("); return; }
    print();
}
void Flixel::play(){
    BlinkM_playScript( addr, 0,0,0 );
}
void Flixel::write(int len, blinkm_script_line* lines){
  printp("Addr: ", addr);
  BlinkM_writeScript( addr, 0, len, 0, lines);
}
// PRINT FUNCTIONS
void Flixel::print(){
  if(!isVerbose) return;
	print( "Flixel attributes: \n");
	printp("  script_id:        ", script);
	printp("  script_reps:      ", reps);
	printp("  script_fadespeed: ", fadespeed);
	printp("  script_timeadj:   ", timeadj);
	printp("  verbose:        ", isVerbose);
}
void Flixel::print(char* c){ if(!isVerbose) return; Serial.println(c);}
void Flixel::printp(char* key, int val){ 
  if(!isVerbose) return; 
  Serial.print(key); 
  Serial.println(val);
}

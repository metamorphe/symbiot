//
//  flixel.h
//  Flixels
//
//  Created by Cesar Torres on 7/2/14.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __Flixels__flixel__
#define __Flixels__flixel__

#include "BlinkM_funcs.h"
#include <string>

class Flixel {
    blinkm_script_line* scripts[10];
public:
    Flixel(int, int, int, int, int);
    void init();
    bool on();
    void print();
    void play();
    void play(String);
    void stop();
    void speed(int);
    void store_script(String, int[]);
    void verbose(bool);
    void print(char*);
    void printp(char*, int);
    void write(int, blinkm_script_line*);

private:
	int addr;
	int script;
	int reps;
	int fadespeed;
	int timeadj;
	bool isVerbose;
};
#endif /* defined(__Flixels__flixel__) */

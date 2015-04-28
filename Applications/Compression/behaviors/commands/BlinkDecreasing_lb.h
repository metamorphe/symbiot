//
//  BlinkDecreasing_lb.h
//  expresso - BlinkDecreasing Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __BlinkDecreasing__expresso__
#define __BlinkDecreasing__expresso__

#include "Logger.h"

	Logger *blink_decreasing;
	void getLog(){
		 blink_decreasing = new Logger( 12, 0, 255);
		blink_decreasing->log(  0,   1);
		blink_decreasing->log(255,  24);
		blink_decreasing->log(  0,  34);
		blink_decreasing->log(255,  45);
		blink_decreasing->log(  0,  56);
		blink_decreasing->log(255,  69);
		blink_decreasing->log(  0,  94);
		blink_decreasing->log(255, 119);
		blink_decreasing->log(  0, 154);
		blink_decreasing->log(255, 188);
		blink_decreasing->log(  0, 246);
		blink_decreasing->log(  0, 298);
	}

#endif /* defined(__BlinkDecreasing__expresso__) */
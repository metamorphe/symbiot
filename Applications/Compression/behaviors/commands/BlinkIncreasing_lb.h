//
//  BlinkIncreasing_lb.h
//  expresso - BlinkIncreasing Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __BlinkIncreasing__expresso__
#define __BlinkIncreasing__expresso__

#include "Logger.h"

	Logger *blink_increasing;
	void getLog(){
		 blink_increasing = new Logger( 11, 0, 255);
		blink_increasing->log(255,  23);
		blink_increasing->log(  0,  80);
		blink_increasing->log(255, 114);
		blink_increasing->log(  0, 150);
		blink_increasing->log(255, 171);
		blink_increasing->log(  0, 199);
		blink_increasing->log(255, 213);
		blink_increasing->log(  0, 224);
		blink_increasing->log(255, 234);
		blink_increasing->log(  0, 245);
		blink_increasing->log(  0, 298);
	}

#endif /* defined(__BlinkIncreasing__expresso__) */
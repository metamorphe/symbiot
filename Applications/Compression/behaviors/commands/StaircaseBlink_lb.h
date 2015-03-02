//
//  StaircaseBlink_lb.h
//  expresso - StaircaseBlink Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __StaircaseBlink__expresso__
#define __StaircaseBlink__expresso__

#include "Logger.h"

	Logger *staircase_blink;
	void getLog(){
		 staircase_blink = new Logger( 10, 0, 255);
		staircase_blink->log(  0,   1);
		staircase_blink->log( 54,  23);
		staircase_blink->log(  3,  62);
		staircase_blink->log(124,  79);
		staircase_blink->log(  0, 119);
		staircase_blink->log(180, 137);
		staircase_blink->log(  0, 176);
		staircase_blink->log(255, 194);
		staircase_blink->log(  0, 228);
		staircase_blink->log(  0, 296);
	}

#endif /* defined(__StaircaseBlink__expresso__) */
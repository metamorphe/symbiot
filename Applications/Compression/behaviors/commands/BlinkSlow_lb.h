//
//  BlinkSlow_lb.h
//  expresso - BlinkSlow Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __BlinkSlow__expresso__
#define __BlinkSlow__expresso__

#include "Logger.h"

	Logger *blink_slow;
	void getLog(){
		 blink_slow = new Logger(  6, 0, 255);
		blink_slow->log(  0,   1);
		blink_slow->log(254,  24);
		blink_slow->log(  0,  94);
		blink_slow->log(255, 164);
		blink_slow->log(  0, 235);
		blink_slow->log(  0, 298);
	}

#endif /* defined(__BlinkSlow__expresso__) */
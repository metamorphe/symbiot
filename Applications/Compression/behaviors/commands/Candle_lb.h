//
//  Candle_lb.h
//  expresso - Candle Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __Candle__expresso__
#define __Candle__expresso__

#include "Logger.h"

	Logger *candle;
	void getLog(){
		 candle = new Logger( 13, 0, 255);
		candle->log(127,  23);
		candle->log(  0,  62);
		candle->log(255,  80);
		candle->log(127, 118);
		candle->log(255, 125);
		candle->log(127, 140);
		candle->log(  0, 164);
		candle->log(127, 186);
		candle->log(255, 207);
		candle->log(127, 246);
		candle->log(  0, 253);
		candle->log(127, 275);
		candle->log(127, 299);
	}

#endif /* defined(__Candle__expresso__) */
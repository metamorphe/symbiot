//
//  Twinkle_lb.h
//  expresso - Twinkle Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __Twinkle__expresso__
#define __Twinkle__expresso__

#include "Logger.h"

	Logger *twinkle;
	void getLog(){
		 twinkle = new Logger( 13, 0, 255);
		twinkle->log(254,  21);
		twinkle->log(107,  42);
		twinkle->log(254,  63);
		twinkle->log(104,  85);
		twinkle->log(  0, 105);
		twinkle->log(254, 127);
		twinkle->log(114, 151);
		twinkle->log(  0, 169);
		twinkle->log(101, 191);
		twinkle->log(255, 212);
		twinkle->log(111, 254);
		twinkle->log(  0, 276);
		twinkle->log(  0, 298);
	}

#endif /* defined(__Twinkle__expresso__) */
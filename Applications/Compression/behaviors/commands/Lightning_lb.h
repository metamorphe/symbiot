//
//  Lightning_lb.h
//  expresso - Lightning Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __Lightning__expresso__
#define __Lightning__expresso__

#include "Logger.h"

	Logger *lightning;
	void getLog(){
		 lightning = new Logger( 16, 0, 255);
		lightning->log(  0,   1);
		lightning->log( 64,  22);
		lightning->log(231,  23);
		lightning->log(255,  24);
		lightning->log( 39,  54);
		lightning->log(110,  65);
		lightning->log(  0,  76);
		lightning->log( 39,  86);
		lightning->log(  0, 101);
		lightning->log(255, 156);
		lightning->log( 38, 192);
		lightning->log(109, 203);
		lightning->log(  0, 214);
		lightning->log( 35, 224);
		lightning->log(  0, 238);
		lightning->log(  0, 294);
	}

#endif /* defined(__Lightning__expresso__) */
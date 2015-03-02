//
//  Raindrops_lb.h
//  expresso - Raindrops Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __Raindrops__expresso__
#define __Raindrops__expresso__

#include "Logger.h"

	Logger *raindrops;
	void getLog(){
		 raindrops = new Logger( 13, 0, 255);
		raindrops->log(154,  21);
		raindrops->log(  0,  46);
		raindrops->log( 62,  71);
		raindrops->log(  0,  92);
		raindrops->log(255, 117);
		raindrops->log(  0, 138);
		raindrops->log(151, 159);
		raindrops->log(  0, 183);
		raindrops->log(239, 205);
		raindrops->log(  0, 229);
		raindrops->log( 67, 251);
		raindrops->log(  0, 274);
		raindrops->log(  0, 298);
	}

#endif /* defined(__Raindrops__expresso__) */
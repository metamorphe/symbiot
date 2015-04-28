//
//  Beacon_lb.h
//  expresso - Beacon Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __Beacon__expresso__
#define __Beacon__expresso__

#include "Logger.h"

	Logger *beacon;
	void getLog(){
		 beacon = new Logger(  2, 0, 255);
		beacon->log(  0,   6);
		beacon->log(  0,  68);
	}

#endif /* defined(__Beacon__expresso__) */
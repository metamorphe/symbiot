//
//  HeartBeat_lb.h
//  expresso - HeartBeat Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __HeartBeat__expresso__
#define __HeartBeat__expresso__

#include "Logger.h"

	Logger *heart_beat;
	void getLog(){
		 heart_beat = new Logger(  9, 0, 255);
		heart_beat->log(255,  19);
		heart_beat->log(  0,  44);
		heart_beat->log(255,  65);
		heart_beat->log(  0,  90);
		heart_beat->log(255, 156);
		heart_beat->log(  0, 182);
		heart_beat->log(255, 203);
		heart_beat->log(  0, 228);
		heart_beat->log(  0, 295);
	}

#endif /* defined(__HeartBeat__expresso__) */
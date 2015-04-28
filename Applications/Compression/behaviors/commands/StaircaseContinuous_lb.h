//
//  StaircaseContinuous_lb.h
//  expresso - StaircaseContinuous Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __StaircaseContinuous__expresso__
#define __StaircaseContinuous__expresso__

#include "Logger.h"

	Logger *staircase_continuous;
	void getLog(){
		 staircase_continuous = new Logger(  6, 0, 255);
		staircase_continuous->log( 58,  20);
		staircase_continuous->log(117,  80);
		staircase_continuous->log(193, 136);
		staircase_continuous->log(255, 193);
		staircase_continuous->log(  0, 250);
		staircase_continuous->log(  0, 296);
	}

#endif /* defined(__StaircaseContinuous__expresso__) */
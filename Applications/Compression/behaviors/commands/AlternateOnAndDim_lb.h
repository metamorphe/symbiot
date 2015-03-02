//
//  AlternateOnAndDim_lb.h
//  expresso - AlternateOnAndDim Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __AlternateOnAndDim__expresso__
#define __AlternateOnAndDim__expresso__

#include "Logger.h"

	Logger *alternate_on_and_dim;
	void getLog(){
		 alternate_on_and_dim = new Logger(  6, 0, 255);
		alternate_on_and_dim->log(  0,   1);
		alternate_on_and_dim->log(255,  21);
		alternate_on_and_dim->log(  0,  94);
		alternate_on_and_dim->log(255, 161);
		alternate_on_and_dim->log(  0, 235);
		alternate_on_and_dim->log(  0, 300);
	}

#endif /* defined(__AlternateOnAndDim__expresso__) */
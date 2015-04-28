//
//  BrightFlash_lb.h
//  expresso - BrightFlash Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __BrightFlash__expresso__
#define __BrightFlash__expresso__

#include "Logger.h"

	Logger *bright_flash;
	void getLog(){
		 bright_flash = new Logger(  2, 0, 255);
		bright_flash->log(  0,   3);
		bright_flash->log(  0, 101);
	}

#endif /* defined(__BrightFlash__expresso__) */
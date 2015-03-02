//
//  OnWithBrightFlash_lb.h
//  expresso - OnWithBrightFlash Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __OnWithBrightFlash__expresso__
#define __OnWithBrightFlash__expresso__

#include "Logger.h"

	Logger *on_with_bright_flash;
	void getLog(){
		 on_with_bright_flash = new Logger(  1, 0, 255);
		on_with_bright_flash->log(  0,  96);
	}

#endif /* defined(__OnWithBrightFlash__expresso__) */
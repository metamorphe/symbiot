//
//  TransmissionRandomBrightness_lb.h
//  expresso - TransmissionRandomBrightness Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __TransmissionRandomBrightness__expresso__
#define __TransmissionRandomBrightness__expresso__

#include "Logger.h"

	Logger *transmission_random_brightness;
	void getLog(){
		 transmission_random_brightness = new Logger( 14, 0, 255);
		transmission_random_brightness->log(186,   1);
		transmission_random_brightness->log(  0,  21);
		transmission_random_brightness->log(129,  53);
		transmission_random_brightness->log(  0,  79);
		transmission_random_brightness->log(255, 113);
		transmission_random_brightness->log(  0, 123);
		transmission_random_brightness->log( 73, 134);
		transmission_random_brightness->log(  0, 159);
		transmission_random_brightness->log(200, 180);
		transmission_random_brightness->log(  0, 204);
		transmission_random_brightness->log(127, 236);
		transmission_random_brightness->log(  0, 250);
		transmission_random_brightness->log(255, 272);
		transmission_random_brightness->log(255, 294);
	}

#endif /* defined(__TransmissionRandomBrightness__expresso__) */
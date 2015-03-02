//
//  TransmissionFixedBrightness_lb.h
//  expresso - TransmissionFixedBrightness Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __TransmissionFixedBrightness__expresso__
#define __TransmissionFixedBrightness__expresso__

#include "Logger.h"

	Logger *transmission_fixed_brightness;
	void getLog(){
		 transmission_fixed_brightness = new Logger( 14, 0, 255);
		transmission_fixed_brightness->log(254,   1);
		transmission_fixed_brightness->log(  0,  25);
		transmission_fixed_brightness->log(254,  58);
		transmission_fixed_brightness->log(  0,  82);
		transmission_fixed_brightness->log(254, 117);
		transmission_fixed_brightness->log(  0, 128);
		transmission_fixed_brightness->log(255, 138);
		transmission_fixed_brightness->log(  0, 163);
		transmission_fixed_brightness->log(255, 184);
		transmission_fixed_brightness->log(  0, 208);
		transmission_fixed_brightness->log(254, 240);
		transmission_fixed_brightness->log(  0, 255);
		transmission_fixed_brightness->log(255, 277);
		transmission_fixed_brightness->log(255, 298);
	}

#endif /* defined(__TransmissionFixedBrightness__expresso__) */
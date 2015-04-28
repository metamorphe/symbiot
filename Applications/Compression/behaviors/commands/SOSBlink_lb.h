//
//  SOSBlink_lb.h
//  expresso - SOSBlink Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __SOSBlink__expresso__
#define __SOSBlink__expresso__

#include "Logger.h"

	Logger *sos_blink;
	void getLog(){
		 sos_blink = new Logger( 19, 0, 255);
		sos_blink->log(255,  13);
		sos_blink->log(  0,  24);
		sos_blink->log(255,  34);
		sos_blink->log(  0,  45);
		sos_blink->log(255,  56);
		sos_blink->log(  0,  66);
		sos_blink->log(255,  87);
		sos_blink->log(  0, 113);
		sos_blink->log(255, 136);
		sos_blink->log(  0, 161);
		sos_blink->log(255, 186);
		sos_blink->log(  0, 210);
		sos_blink->log(255, 233);
		sos_blink->log(  0, 242);
		sos_blink->log(255, 252);
		sos_blink->log(  0, 263);
		sos_blink->log(255, 275);
		sos_blink->log(  0, 285);
		sos_blink->log(  0, 296);
	}

#endif /* defined(__SOSBlink__expresso__) */
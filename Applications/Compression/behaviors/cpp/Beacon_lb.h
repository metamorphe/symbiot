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

blinkm_script_line Beacon[] = {
	{ 6, { 'n', 0x00,0x00,0x00}},
	{ 62, { 'n', 0x00,0x00,0x00}}
};
int script_beacon_len = 2;  // number of script lines above

#endif /* defined(__Beacon__expresso__) */
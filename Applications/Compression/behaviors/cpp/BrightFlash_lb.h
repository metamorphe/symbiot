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

blinkm_script_line BrightFlash[] = {
	{ 3, { 'n', 0x00,0x00,0x00}},
	{ 98, { 'n', 0x00,0x00,0x00}}
};
int script_brightflash_len = 2;  // number of script lines above

#endif /* defined(__BrightFlash__expresso__) */
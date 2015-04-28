//
//  BlinkSlow_lb.h
//  expresso - BlinkSlow Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __BlinkSlow__expresso__
#define __BlinkSlow__expresso__

#include "Logger.h"

blinkm_script_line BlinkSlow[] = {
	{ 1, { 'n', 0x00,0x00,0x00}},
	{ 23, { 'n', 0xfe,0xfe,0xfe}},
	{ 70, { 'n', 0x00,0x00,0x00}},
	{ 70, { 'n', 0xff,0xff,0xff}},
	{ 71, { 'n', 0x00,0x00,0x00}},
	{ 63, { 'n', 0x00,0x00,0x00}}
};
int script_blinkslow_len = 6;  // number of script lines above

#endif /* defined(__BlinkSlow__expresso__) */
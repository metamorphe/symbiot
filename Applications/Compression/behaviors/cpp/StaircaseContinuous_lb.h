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

blinkm_script_line StaircaseContinuous[] = {
	{ 20, { 'n', 0x3a,0x3a,0x3a}},
	{ 60, { 'n', 0x75,0x75,0x75}},
	{ 56, { 'n', 0xc1,0xc1,0xc1}},
	{ 57, { 'n', 0xff,0xff,0xff}},
	{ 57, { 'n', 0x00,0x00,0x00}},
	{ 46, { 'n', 0x00,0x00,0x00}}
};
int script_staircasecontinuous_len = 6;  // number of script lines above

#endif /* defined(__StaircaseContinuous__expresso__) */
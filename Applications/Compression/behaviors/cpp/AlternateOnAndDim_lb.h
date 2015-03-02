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

blinkm_script_line AlternateOnAndDim[] = {
	{ 1, { 'n', 0x00,0x00,0x00}},
	{ 20, { 'n', 0xff,0xff,0xff}},
	{ 73, { 'n', 0x00,0x00,0x00}},
	{ 67, { 'n', 0xff,0xff,0xff}},
	{ 74, { 'n', 0x00,0x00,0x00}},
	{ 65, { 'n', 0x00,0x00,0x00}}
};
int script_alternateonanddim_len = 6;  // number of script lines above

#endif /* defined(__AlternateOnAndDim__expresso__) */
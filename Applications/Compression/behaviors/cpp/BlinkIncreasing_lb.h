//
//  BlinkIncreasing_lb.h
//  expresso - BlinkIncreasing Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __BlinkIncreasing__expresso__
#define __BlinkIncreasing__expresso__

#include "Logger.h"

blinkm_script_line BlinkIncreasing[] = {
	{ 23, { 'n', 0xff,0xff,0xff}},
	{ 57, { 'n', 0x00,0x00,0x00}},
	{ 34, { 'n', 0xff,0xff,0xff}},
	{ 36, { 'n', 0x00,0x00,0x00}},
	{ 21, { 'n', 0xff,0xff,0xff}},
	{ 28, { 'n', 0x00,0x00,0x00}},
	{ 14, { 'n', 0xff,0xff,0xff}},
	{ 11, { 'n', 0x00,0x00,0x00}},
	{ 10, { 'n', 0xff,0xff,0xff}},
	{ 11, { 'n', 0x00,0x00,0x00}},
	{ 53, { 'n', 0x00,0x00,0x00}}
};
int script_blinkincreasing_len = 11;  // number of script lines above

#endif /* defined(__BlinkIncreasing__expresso__) */
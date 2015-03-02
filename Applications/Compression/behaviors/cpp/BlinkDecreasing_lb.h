//
//  BlinkDecreasing_lb.h
//  expresso - BlinkDecreasing Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __BlinkDecreasing__expresso__
#define __BlinkDecreasing__expresso__

#include "Logger.h"

blinkm_script_line BlinkDecreasing[] = {
	{ 1, { 'n', 0x00,0x00,0x00}},
	{ 23, { 'n', 0xff,0xff,0xff}},
	{ 10, { 'n', 0x00,0x00,0x00}},
	{ 11, { 'n', 0xff,0xff,0xff}},
	{ 11, { 'n', 0x00,0x00,0x00}},
	{ 13, { 'n', 0xff,0xff,0xff}},
	{ 25, { 'n', 0x00,0x00,0x00}},
	{ 25, { 'n', 0xff,0xff,0xff}},
	{ 35, { 'n', 0x00,0x00,0x00}},
	{ 34, { 'n', 0xff,0xff,0xff}},
	{ 58, { 'n', 0x00,0x00,0x00}},
	{ 52, { 'n', 0x00,0x00,0x00}}
};
int script_blinkdecreasing_len = 12;  // number of script lines above

#endif /* defined(__BlinkDecreasing__expresso__) */
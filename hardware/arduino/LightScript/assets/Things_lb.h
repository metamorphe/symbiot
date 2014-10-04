//
//  Things_lb.h
//  Flixels - Things Behavior
//
//  Created by Cesar Torres on 7/2/14.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __Things__flixel__
#define __Things__flixel__

#include "BlinkM_funcs.h"
blinkm_script_line Things[] = {
	{ 1, { 'n', 0xfe,0xfe,0xfe}},
	{ 23, { 'n', 0x00,0x00,0x00}},
	{ 70, { 'n', 0xff,0xff,0xff}},
	{ 70, { 'n', 0x00,0x00,0x00}},
	{ 71, { 'n', 0xff,0xff,0xff}},
	{ 63, { 'n', 0xff,0xff,0xff}}
};
int script_things_len = 5;  // number of script lines above
#endif /* defined(__Things__flixel__) */
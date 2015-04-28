//
//  TransmissionRandomBrightness_lb.h
//  expresso - TransmissionRandomBrightness Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __TransmissionRandomBrightness__expresso__
#define __TransmissionRandomBrightness__expresso__

#include "Logger.h"

blinkm_script_line TransmissionRandomBrightness[] = {
	{ 1, { 'n', 0xba,0xba,0xba}},
	{ 20, { 'n', 0x00,0x00,0x00}},
	{ 32, { 'n', 0x81,0x81,0x81}},
	{ 26, { 'n', 0x00,0x00,0x00}},
	{ 34, { 'n', 0xff,0xff,0xff}},
	{ 10, { 'n', 0x00,0x00,0x00}},
	{ 11, { 'n', 0x49,0x49,0x49}},
	{ 25, { 'n', 0x00,0x00,0x00}},
	{ 21, { 'n', 0xc8,0xc8,0xc8}},
	{ 24, { 'n', 0x00,0x00,0x00}},
	{ 32, { 'n', 0x7f,0x7f,0x7f}},
	{ 14, { 'n', 0x00,0x00,0x00}},
	{ 22, { 'n', 0xff,0xff,0xff}},
	{ 22, { 'n', 0xff,0xff,0xff}}
};
int script_transmissionrandombrightness_len = 14;  // number of script lines above

#endif /* defined(__TransmissionRandomBrightness__expresso__) */
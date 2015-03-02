//
//  TransmissionFixedBrightness_lb.h
//  expresso - TransmissionFixedBrightness Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __TransmissionFixedBrightness__expresso__
#define __TransmissionFixedBrightness__expresso__

#include "Logger.h"

blinkm_script_line TransmissionFixedBrightness[] = {
	{ 1, { 'n', 0xfe,0xfe,0xfe}},
	{ 24, { 'n', 0x00,0x00,0x00}},
	{ 33, { 'n', 0xfe,0xfe,0xfe}},
	{ 24, { 'n', 0x00,0x00,0x00}},
	{ 35, { 'n', 0xfe,0xfe,0xfe}},
	{ 11, { 'n', 0x00,0x00,0x00}},
	{ 10, { 'n', 0xff,0xff,0xff}},
	{ 25, { 'n', 0x00,0x00,0x00}},
	{ 21, { 'n', 0xff,0xff,0xff}},
	{ 24, { 'n', 0x00,0x00,0x00}},
	{ 32, { 'n', 0xfe,0xfe,0xfe}},
	{ 15, { 'n', 0x00,0x00,0x00}},
	{ 22, { 'n', 0xff,0xff,0xff}},
	{ 21, { 'n', 0xff,0xff,0xff}}
};
int script_transmissionfixedbrightness_len = 14;  // number of script lines above

#endif /* defined(__TransmissionFixedBrightness__expresso__) */
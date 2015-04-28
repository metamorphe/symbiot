//
//  HeartBeat_lb.h
//  expresso - HeartBeat Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __HeartBeat__expresso__
#define __HeartBeat__expresso__

#include "Logger.h"

blinkm_script_line HeartBeat[] = {
	{ 19, { 'n', 0xff,0xff,0xff}},
	{ 25, { 'n', 0x00,0x00,0x00}},
	{ 21, { 'n', 0xff,0xff,0xff}},
	{ 25, { 'n', 0x00,0x00,0x00}},
	{ 66, { 'n', 0xff,0xff,0xff}},
	{ 26, { 'n', 0x00,0x00,0x00}},
	{ 21, { 'n', 0xff,0xff,0xff}},
	{ 25, { 'n', 0x00,0x00,0x00}},
	{ 67, { 'n', 0x00,0x00,0x00}}
};
int script_heartbeat_len = 9;  // number of script lines above

#endif /* defined(__HeartBeat__expresso__) */
//
//  Raindrops_lb.h
//  expresso - Raindrops Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __Raindrops__expresso__
#define __Raindrops__expresso__

#include "Logger.h"

blinkm_script_line Raindrops[] = {
	{ 21, { 'n', 0x9a,0x9a,0x9a}},
	{ 25, { 'n', 0x00,0x00,0x00}},
	{ 25, { 'n', 0x3e,0x3e,0x3e}},
	{ 21, { 'n', 0x00,0x00,0x00}},
	{ 25, { 'n', 0xff,0xff,0xff}},
	{ 21, { 'n', 0x00,0x00,0x00}},
	{ 21, { 'n', 0x97,0x97,0x97}},
	{ 24, { 'n', 0x00,0x00,0x00}},
	{ 22, { 'n', 0xef,0xef,0xef}},
	{ 24, { 'n', 0x00,0x00,0x00}},
	{ 22, { 'n', 0x43,0x43,0x43}},
	{ 23, { 'n', 0x00,0x00,0x00}},
	{ 24, { 'n', 0x00,0x00,0x00}}
};
int script_raindrops_len = 13;  // number of script lines above

#endif /* defined(__Raindrops__expresso__) */
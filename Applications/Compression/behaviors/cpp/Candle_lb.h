//
//  Candle_lb.h
//  expresso - Candle Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __Candle__expresso__
#define __Candle__expresso__

#include "Logger.h"

blinkm_script_line Candle[] = {
	{ 23, { 'n', 0x7f,0x7f,0x7f}},
	{ 39, { 'n', 0x00,0x00,0x00}},
	{ 18, { 'n', 0xff,0xff,0xff}},
	{ 38, { 'n', 0x7f,0x7f,0x7f}},
	{ 7, { 'n', 0xff,0xff,0xff}},
	{ 15, { 'n', 0x7f,0x7f,0x7f}},
	{ 24, { 'n', 0x00,0x00,0x00}},
	{ 22, { 'n', 0x7f,0x7f,0x7f}},
	{ 21, { 'n', 0xff,0xff,0xff}},
	{ 39, { 'n', 0x7f,0x7f,0x7f}},
	{ 7, { 'n', 0x00,0x00,0x00}},
	{ 22, { 'n', 0x7f,0x7f,0x7f}},
	{ 24, { 'n', 0x7f,0x7f,0x7f}}
};
int script_candle_len = 13;  // number of script lines above

#endif /* defined(__Candle__expresso__) */
//
//  StaircaseBlink_lb.h
//  expresso - StaircaseBlink Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __StaircaseBlink__expresso__
#define __StaircaseBlink__expresso__

#include "Logger.h"

blinkm_script_line StaircaseBlink[] = {
	{ 1, { 'n', 0x00,0x00,0x00}},
	{ 22, { 'n', 0x36,0x36,0x36}},
	{ 39, { 'n', 0x03,0x03,0x03}},
	{ 17, { 'n', 0x7c,0x7c,0x7c}},
	{ 40, { 'n', 0x00,0x00,0x00}},
	{ 18, { 'n', 0xb4,0xb4,0xb4}},
	{ 39, { 'n', 0x00,0x00,0x00}},
	{ 18, { 'n', 0xff,0xff,0xff}},
	{ 34, { 'n', 0x00,0x00,0x00}},
	{ 68, { 'n', 0x00,0x00,0x00}}
};
int script_staircaseblink_len = 10;  // number of script lines above

#endif /* defined(__StaircaseBlink__expresso__) */
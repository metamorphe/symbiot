//
//  Twinkle_lb.h
//  expresso - Twinkle Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __Twinkle__expresso__
#define __Twinkle__expresso__

#include "Logger.h"

blinkm_script_line Twinkle[] = {
	{ 21, { 'n', 0xfe,0xfe,0xfe}},
	{ 21, { 'n', 0x6b,0x6b,0x6b}},
	{ 21, { 'n', 0xfe,0xfe,0xfe}},
	{ 22, { 'n', 0x68,0x68,0x68}},
	{ 20, { 'n', 0x00,0x00,0x00}},
	{ 22, { 'n', 0xfe,0xfe,0xfe}},
	{ 24, { 'n', 0x72,0x72,0x72}},
	{ 18, { 'n', 0x00,0x00,0x00}},
	{ 22, { 'n', 0x65,0x65,0x65}},
	{ 21, { 'n', 0xff,0xff,0xff}},
	{ 42, { 'n', 0x6f,0x6f,0x6f}},
	{ 22, { 'n', 0x00,0x00,0x00}},
	{ 22, { 'n', 0x00,0x00,0x00}}
};
int script_twinkle_len = 13;  // number of script lines above

#endif /* defined(__Twinkle__expresso__) */
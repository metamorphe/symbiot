//
//  FastInSlowOut_lb.h
//  expresso - FastInSlowOut Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __FastInSlowOut__expresso__
#define __FastInSlowOut__expresso__

#include "Logger.h"

blinkm_script_line FastInSlowOut[] = {
	{ 1, { 'n', 0x05,0x05,0x05}},
	{ 1, { 'n', 0x04,0x04,0x04}},
	{ 1, { 'n', 0x03,0x03,0x03}},
	{ 1, { 'n', 0x02,0x02,0x02}},
	{ 1, { 'n', 0x01,0x01,0x01}},
	{ 2, { 'n', 0x00,0x00,0x00}},
	{ 7, { 'n', 0x01,0x01,0x01}},
	{ 2, { 'n', 0x02,0x02,0x02}},
	{ 1, { 'n', 0x03,0x03,0x03}},
	{ 1, { 'n', 0x05,0x05,0x05}},
	{ 1, { 'n', 0x06,0x06,0x06}},
	{ 1, { 'n', 0x08,0x08,0x08}},
	{ 1, { 'n', 0x09,0x09,0x09}},
	{ 1, { 'n', 0x0b,0x0b,0x0b}},
	{ 1, { 'n', 0x0e,0x0e,0x0e}},
	{ 1, { 'n', 0x10,0x10,0x10}},
	{ 1, { 'n', 0x13,0x13,0x13}},
	{ 1, { 'n', 0x16,0x16,0x16}},
	{ 1, { 'n', 0x1a,0x1a,0x1a}},
	{ 1, { 'n', 0x1e,0x1e,0x1e}},
	{ 1, { 'n', 0x22,0x22,0x22}},
	{ 1, { 'n', 0x27,0x27,0x27}},
	{ 1, { 'n', 0x2c,0x2c,0x2c}},
	{ 1, { 'n', 0x32,0x32,0x32}},
	{ 1, { 'n', 0x39,0x39,0x39}},
	{ 1, { 'n', 0x40,0x40,0x40}},
	{ 1, { 'n', 0x49,0x49,0x49}},
	{ 1, { 'n', 0x52,0x52,0x52}},
	{ 1, { 'n', 0x5e,0x5e,0x5e}},
	{ 1, { 'n', 0x6b,0x6b,0x6b}},
	{ 1, { 'n', 0x78,0x78,0x78}},
	{ 1, { 'n', 0x84,0x84,0x84}},
	{ 1, { 'n', 0x90,0x90,0x90}},
	{ 1, { 'n', 0x9b,0x9b,0x9b}},
	{ 1, { 'n', 0xa5,0xa5,0xa5}},
	{ 1, { 'n', 0xaf,0xaf,0xaf}},
	{ 1, { 'n', 0xb8,0xb8,0xb8}},
	{ 1, { 'n', 0xc1,0xc1,0xc1}},
	{ 1, { 'n', 0xc9,0xc9,0xc9}},
	{ 1, { 'n', 0xd1,0xd1,0xd1}},
	{ 1, { 'n', 0xd8,0xd8,0xd8}},
	{ 1, { 'n', 0xdf,0xdf,0xdf}},
	{ 1, { 'n', 0xe5,0xe5,0xe5}},
	{ 1, { 'n', 0xea,0xea,0xea}},
	{ 1, { 'n', 0xef,0xef,0xef}},
	{ 1, { 'n', 0xf4,0xf4,0xf4}},
	{ 1, { 'n', 0xf7,0xf7,0xf7}},
	{ 1, { 'n', 0xfa,0xfa,0xfa}},
	{ 1, { 'n', 0xfd,0xfd,0xfd}},
	{ 1, { 'n', 0xfe,0xfe,0xfe}},
	{ 3, { 'n', 0xfd,0xfd,0xfd}},
	{ 1, { 'n', 0xfc,0xfc,0xfc}},
	{ 1, { 'n', 0xfb,0xfb,0xfb}},
	{ 1, { 'n', 0xf9,0xf9,0xf9}},
	{ 1, { 'n', 0xf7,0xf7,0xf7}},
	{ 1, { 'n', 0xf5,0xf5,0xf5}},
	{ 1, { 'n', 0xf3,0xf3,0xf3}},
	{ 1, { 'n', 0xf0,0xf0,0xf0}},
	{ 1, { 'n', 0xed,0xed,0xed}},
	{ 1, { 'n', 0xeb,0xeb,0xeb}},
	{ 1, { 'n', 0xe8,0xe8,0xe8}},
	{ 1, { 'n', 0xe5,0xe5,0xe5}},
	{ 1, { 'n', 0xe2,0xe2,0xe2}},
	{ 1, { 'n', 0xde,0xde,0xde}},
	{ 1, { 'n', 0xdb,0xdb,0xdb}},
	{ 1, { 'n', 0xd8,0xd8,0xd8}},
	{ 1, { 'n', 0xd4,0xd4,0xd4}},
	{ 1, { 'n', 0xd1,0xd1,0xd1}},
	{ 1, { 'n', 0xcd,0xcd,0xcd}},
	{ 1, { 'n', 0xc9,0xc9,0xc9}},
	{ 1, { 'n', 0xc6,0xc6,0xc6}},
	{ 1, { 'n', 0xc2,0xc2,0xc2}},
	{ 1, { 'n', 0xbe,0xbe,0xbe}},
	{ 1, { 'n', 0xba,0xba,0xba}},
	{ 1, { 'n', 0xb6,0xb6,0xb6}},
	{ 1, { 'n', 0xb2,0xb2,0xb2}},
	{ 1, { 'n', 0xae,0xae,0xae}},
	{ 1, { 'n', 0xaa,0xaa,0xaa}},
	{ 1, { 'n', 0xa6,0xa6,0xa6}},
	{ 1, { 'n', 0xa1,0xa1,0xa1}},
	{ 1, { 'n', 0x9d,0x9d,0x9d}},
	{ 1, { 'n', 0x99,0x99,0x99}},
	{ 1, { 'n', 0x94,0x94,0x94}},
	{ 1, { 'n', 0x90,0x90,0x90}},
	{ 1, { 'n', 0x8b,0x8b,0x8b}},
	{ 1, { 'n', 0x87,0x87,0x87}},
	{ 1, { 'n', 0x82,0x82,0x82}},
	{ 1, { 'n', 0x7e,0x7e,0x7e}},
	{ 1, { 'n', 0x79,0x79,0x79}},
	{ 1, { 'n', 0x75,0x75,0x75}},
	{ 1, { 'n', 0x70,0x70,0x70}},
	{ 1, { 'n', 0x6b,0x6b,0x6b}},
	{ 1, { 'n', 0x66,0x66,0x66}},
	{ 1, { 'n', 0x62,0x62,0x62}},
	{ 1, { 'n', 0x5d,0x5d,0x5d}},
	{ 1, { 'n', 0x58,0x58,0x58}},
	{ 1, { 'n', 0x53,0x53,0x53}},
	{ 1, { 'n', 0x4e,0x4e,0x4e}},
	{ 1, { 'n', 0x4a,0x4a,0x4a}},
	{ 1, { 'n', 0x45,0x45,0x45}},
	{ 1, { 'n', 0x41,0x41,0x41}},
	{ 1, { 'n', 0x3d,0x3d,0x3d}},
	{ 1, { 'n', 0x39,0x39,0x39}},
	{ 1, { 'n', 0x35,0x35,0x35}},
	{ 1, { 'n', 0x31,0x31,0x31}},
	{ 1, { 'n', 0x2e,0x2e,0x2e}},
	{ 1, { 'n', 0x2b,0x2b,0x2b}},
	{ 1, { 'n', 0x28,0x28,0x28}},
	{ 1, { 'n', 0x25,0x25,0x25}},
	{ 1, { 'n', 0x22,0x22,0x22}},
	{ 1, { 'n', 0x1f,0x1f,0x1f}},
	{ 1, { 'n', 0x1d,0x1d,0x1d}},
	{ 1, { 'n', 0x1a,0x1a,0x1a}},
	{ 1, { 'n', 0x18,0x18,0x18}},
	{ 1, { 'n', 0x16,0x16,0x16}},
	{ 1, { 'n', 0x14,0x14,0x14}},
	{ 1, { 'n', 0x13,0x13,0x13}},
	{ 1, { 'n', 0x11,0x11,0x11}},
	{ 1, { 'n', 0x0f,0x0f,0x0f}},
	{ 1, { 'n', 0x0e,0x0e,0x0e}},
	{ 1, { 'n', 0x0d,0x0d,0x0d}},
	{ 1, { 'n', 0x0b,0x0b,0x0b}},
	{ 1, { 'n', 0x0a,0x0a,0x0a}},
	{ 1, { 'n', 0x09,0x09,0x09}},
	{ 1, { 'n', 0x08,0x08,0x08}},
	{ 1, { 'n', 0x07,0x07,0x07}},
	{ 2, { 'n', 0x06,0x06,0x06}},
	{ 1, { 'n', 0x05,0x05,0x05}},
	{ 2, { 'n', 0x04,0x04,0x04}},
	{ 3, { 'n', 0x03,0x03,0x03}},
	{ 9, { 'n', 0x04,0x04,0x04}},
	{ 2, { 'n', 0x05,0x05,0x05}},
	{ 1, { 'n', 0x06,0x06,0x06}},
	{ 2, { 'n', 0x07,0x07,0x07}},
	{ 1, { 'n', 0x09,0x09,0x09}},
	{ 1, { 'n', 0x0a,0x0a,0x0a}},
	{ 1, { 'n', 0x0c,0x0c,0x0c}},
	{ 1, { 'n', 0x0d,0x0d,0x0d}},
	{ 1, { 'n', 0x0f,0x0f,0x0f}},
	{ 1, { 'n', 0x12,0x12,0x12}},
	{ 1, { 'n', 0x14,0x14,0x14}},
	{ 1, { 'n', 0x17,0x17,0x17}},
	{ 1, { 'n', 0x1a,0x1a,0x1a}},
	{ 1, { 'n', 0x1d,0x1d,0x1d}},
	{ 1, { 'n', 0x21,0x21,0x21}},
	{ 1, { 'n', 0x25,0x25,0x25}},
	{ 1, { 'n', 0x2a,0x2a,0x2a}},
	{ 1, { 'n', 0x2f,0x2f,0x2f}},
	{ 1, { 'n', 0x35,0x35,0x35}},
	{ 1, { 'n', 0x3c,0x3c,0x3c}},
	{ 1, { 'n', 0x44,0x44,0x44}},
	{ 1, { 'n', 0x4d,0x4d,0x4d}},
	{ 1, { 'n', 0x58,0x58,0x58}},
	{ 1, { 'n', 0x66,0x66,0x66}},
	{ 1, { 'n', 0x76,0x76,0x76}},
	{ 1, { 'n', 0x8b,0x8b,0x8b}},
	{ 1, { 'n', 0x9f,0x9f,0x9f}},
	{ 1, { 'n', 0xae,0xae,0xae}},
	{ 1, { 'n', 0xba,0xba,0xba}},
	{ 1, { 'n', 0xc5,0xc5,0xc5}},
	{ 1, { 'n', 0xce,0xce,0xce}},
	{ 1, { 'n', 0xd5,0xd5,0xd5}},
	{ 1, { 'n', 0xdc,0xdc,0xdc}},
	{ 1, { 'n', 0xe2,0xe2,0xe2}},
	{ 1, { 'n', 0xe8,0xe8,0xe8}},
	{ 1, { 'n', 0xec,0xec,0xec}},
	{ 1, { 'n', 0xf0,0xf0,0xf0}},
	{ 1, { 'n', 0xf3,0xf3,0xf3}},
	{ 1, { 'n', 0xf6,0xf6,0xf6}},
	{ 1, { 'n', 0xf9,0xf9,0xf9}},
	{ 1, { 'n', 0xfb,0xfb,0xfb}},
	{ 1, { 'n', 0xfc,0xfc,0xfc}},
	{ 1, { 'n', 0xfd,0xfd,0xfd}},
	{ 1, { 'n', 0xfe,0xfe,0xfe}},
	{ 1, { 'n', 0xff,0xff,0xff}},
	{ 1, { 'n', 0xfe,0xfe,0xfe}},
	{ 2, { 'n', 0xfd,0xfd,0xfd}},
	{ 1, { 'n', 0xfb,0xfb,0xfb}},
	{ 1, { 'n', 0xfa,0xfa,0xfa}},
	{ 1, { 'n', 0xf8,0xf8,0xf8}},
	{ 1, { 'n', 0xf6,0xf6,0xf6}},
	{ 1, { 'n', 0xf4,0xf4,0xf4}},
	{ 1, { 'n', 0xf1,0xf1,0xf1}},
	{ 1, { 'n', 0xef,0xef,0xef}},
	{ 1, { 'n', 0xec,0xec,0xec}},
	{ 1, { 'n', 0xe9,0xe9,0xe9}},
	{ 1, { 'n', 0xe6,0xe6,0xe6}},
	{ 1, { 'n', 0xe3,0xe3,0xe3}},
	{ 1, { 'n', 0xe0,0xe0,0xe0}},
	{ 1, { 'n', 0xdd,0xdd,0xdd}},
	{ 1, { 'n', 0xda,0xda,0xda}},
	{ 1, { 'n', 0xd6,0xd6,0xd6}},
	{ 1, { 'n', 0xd3,0xd3,0xd3}},
	{ 1, { 'n', 0xcf,0xcf,0xcf}},
	{ 1, { 'n', 0xcb,0xcb,0xcb}},
	{ 1, { 'n', 0xc7,0xc7,0xc7}},
	{ 1, { 'n', 0xc4,0xc4,0xc4}},
	{ 1, { 'n', 0xc0,0xc0,0xc0}},
	{ 1, { 'n', 0xbc,0xbc,0xbc}},
	{ 1, { 'n', 0xb7,0xb7,0xb7}},
	{ 1, { 'n', 0xb3,0xb3,0xb3}},
	{ 1, { 'n', 0xaf,0xaf,0xaf}},
	{ 1, { 'n', 0xab,0xab,0xab}},
	{ 1, { 'n', 0xa7,0xa7,0xa7}},
	{ 1, { 'n', 0xa2,0xa2,0xa2}},
	{ 1, { 'n', 0x9e,0x9e,0x9e}},
	{ 1, { 'n', 0x99,0x99,0x99}},
	{ 1, { 'n', 0x95,0x95,0x95}},
	{ 1, { 'n', 0x90,0x90,0x90}},
	{ 1, { 'n', 0x8b,0x8b,0x8b}},
	{ 1, { 'n', 0x86,0x86,0x86}},
	{ 1, { 'n', 0x81,0x81,0x81}},
	{ 1, { 'n', 0x7c,0x7c,0x7c}},
	{ 1, { 'n', 0x77,0x77,0x77}},
	{ 1, { 'n', 0x73,0x73,0x73}},
	{ 1, { 'n', 0x6e,0x6e,0x6e}},
	{ 1, { 'n', 0x6a,0x6a,0x6a}},
	{ 1, { 'n', 0x65,0x65,0x65}},
	{ 1, { 'n', 0x61,0x61,0x61}},
	{ 1, { 'n', 0x5d,0x5d,0x5d}},
	{ 1, { 'n', 0x59,0x59,0x59}},
	{ 1, { 'n', 0x55,0x55,0x55}},
	{ 1, { 'n', 0x51,0x51,0x51}},
	{ 1, { 'n', 0x4e,0x4e,0x4e}},
	{ 1, { 'n', 0x4a,0x4a,0x4a}},
	{ 1, { 'n', 0x46,0x46,0x46}},
	{ 1, { 'n', 0x43,0x43,0x43}},
	{ 1, { 'n', 0x40,0x40,0x40}},
	{ 1, { 'n', 0x3c,0x3c,0x3c}},
	{ 1, { 'n', 0x39,0x39,0x39}},
	{ 1, { 'n', 0x36,0x36,0x36}},
	{ 1, { 'n', 0x33,0x33,0x33}},
	{ 1, { 'n', 0x30,0x30,0x30}},
	{ 1, { 'n', 0x2d,0x2d,0x2d}},
	{ 1, { 'n', 0x2a,0x2a,0x2a}},
	{ 1, { 'n', 0x27,0x27,0x27}},
	{ 1, { 'n', 0x25,0x25,0x25}},
	{ 1, { 'n', 0x22,0x22,0x22}},
	{ 1, { 'n', 0x20,0x20,0x20}},
	{ 1, { 'n', 0x1d,0x1d,0x1d}},
	{ 1, { 'n', 0x1b,0x1b,0x1b}},
	{ 1, { 'n', 0x19,0x19,0x19}},
	{ 1, { 'n', 0x17,0x17,0x17}},
	{ 1, { 'n', 0x15,0x15,0x15}},
	{ 1, { 'n', 0x13,0x13,0x13}},
	{ 1, { 'n', 0x11,0x11,0x11}},
	{ 1, { 'n', 0x0f,0x0f,0x0f}},
	{ 1, { 'n', 0x0e,0x0e,0x0e}},
	{ 1, { 'n', 0x0c,0x0c,0x0c}},
	{ 1, { 'n', 0x0b,0x0b,0x0b}},
	{ 1, { 'n', 0x09,0x09,0x09}},
	{ 1, { 'n', 0x08,0x08,0x08}},
	{ 1, { 'n', 0x07,0x07,0x07}},
	{ 1, { 'n', 0x06,0x06,0x06}},
	{ 1, { 'n', 0x05,0x05,0x05}},
	{ 2, { 'n', 0x04,0x04,0x04}},
	{ 1, { 'n', 0x03,0x03,0x03}},
	{ 8, { 'n', 0x04,0x04,0x04}},
	{ 1, { 'n', 0x05,0x05,0x05}}
};
int script_fastinslowout_len = 259;  // number of script lines above

#endif /* defined(__FastInSlowOut__expresso__) */
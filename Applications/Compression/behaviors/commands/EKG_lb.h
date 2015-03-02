//
//  EKG_lb.h
//  expresso - EKG Behavior
//
//  Created by Cesar Torres on 11/14/2014.
//  Copyright (c) 2014 Cesar Torres. All rights reserved.
//

#ifndef __EKG__expresso__
#define __EKG__expresso__

#include "Logger.h"

	Logger *ekg;
	void getLog(){
		 ekg = new Logger( 77, 0, 255);
		ekg->log(134,   1);
		ekg->log(136,  29);
		ekg->log(146,  30);
		ekg->log(156,  31);
		ekg->log(166,  32);
		ekg->log(176,  33);
		ekg->log(186,  34);
		ekg->log(196,  35);
		ekg->log(206,  36);
		ekg->log(216,  37);
		ekg->log(226,  38);
		ekg->log(235,  39);
		ekg->log(245,  40);
		ekg->log(232,  41);
		ekg->log(212,  42);
		ekg->log(193,  43);
		ekg->log(173,  44);
		ekg->log(153,  45);
		ekg->log(133,  46);
		ekg->log(113,  47);
		ekg->log( 94,  48);
		ekg->log( 74,  49);
		ekg->log( 54,  50);
		ekg->log( 34,  51);
		ekg->log( 14,  52);
		ekg->log(  0,  53);
		ekg->log( 11,  54);
		ekg->log( 23,  55);
		ekg->log( 35,  56);
		ekg->log( 47,  57);
		ekg->log( 59,  58);
		ekg->log( 71,  59);
		ekg->log( 83,  60);
		ekg->log( 94,  61);
		ekg->log(106,  62);
		ekg->log(118,  63);
		ekg->log(130,  64);
		ekg->log(133,  65);
		ekg->log(134, 107);
		ekg->log(144, 166);
		ekg->log(155, 167);
		ekg->log(166, 168);
		ekg->log(177, 169);
		ekg->log(188, 170);
		ekg->log(199, 171);
		ekg->log(210, 172);
		ekg->log(221, 173);
		ekg->log(232, 174);
		ekg->log(243, 175);
		ekg->log(255, 176);
		ekg->log(238, 177);
		ekg->log(217, 178);
		ekg->log(196, 179);
		ekg->log(175, 180);
		ekg->log(153, 181);
		ekg->log(132, 182);
		ekg->log(111, 183);
		ekg->log( 90, 184);
		ekg->log( 69, 185);
		ekg->log( 47, 186);
		ekg->log( 26, 187);
		ekg->log(  5, 188);
		ekg->log( 17, 190);
		ekg->log( 28, 191);
		ekg->log( 40, 192);
		ekg->log( 52, 193);
		ekg->log( 63, 194);
		ekg->log( 75, 195);
		ekg->log( 86, 196);
		ekg->log( 98, 197);
		ekg->log(110, 198);
		ekg->log(121, 199);
		ekg->log(133, 200);
		ekg->log(134, 201);
		ekg->log(135, 202);
		ekg->log(136, 260);
		ekg->log(136, 299);
	}

#endif /* defined(__EKG__expresso__) */
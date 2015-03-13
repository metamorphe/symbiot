/**
 * Behavior.h
 * 
 * More info goes here
 *
 */

#ifndef Behavior_h
#define Behavior_h

#include "Arduino.h"
#include "BlinkM_funcs.h"

class Behavior {

	public:
		Behavior(blinkm_script_line scriptArr[]);
		void setLines(blinkm_script_line scriptArr[]);
		blinkm_script_line *getLines(void);
		void setLine(uint8_t lineNum, blinkm_script_line line);
		blinkm_script_line getLine(uint8_t lineNum);
	
	private:
		blinkm_script_line _scriptArr[];

};

#endif

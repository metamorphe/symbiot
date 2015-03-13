/**
 * BeanSocket.h
 * 
 * More info goes here
 *
 */

#ifndef BeanSocket_h
#define BeanSocket_h

#include "Arduino.h"
#include "Bean.h"
#include "Behavior.h"
#include <RF24.h>

class BeanSocket {

	public:
                BeanSocket(void);
		BeanSocket(Bean bean);
		void send(Behavior behavior);
		void receive(void);
		Bean getBean(void);
	
	private:
		Bean _bean;
		RF24 _radio;
		uint64_t _pipes[2];
		uint8_t _numLines;
		blinkm_script_line READ_BUF[256];
		int _blinkmAddr;

};
#endif


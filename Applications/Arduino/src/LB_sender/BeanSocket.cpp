/**
 * BeanSocket.cpp
 * 
 * More info goes here
 *
 * Dependencies:
 * -- BlinkM: Wire.h, BlinkM_funcs.h
 * -- rF: SPI.h, RF24.h (radio), nRF24L01.h (network layer)
 *
 */

#include "Arduino.h"
#include "BeanSocket.h"
#include <Wire.h">
#include "BlinkM_funcs.h"
#include <SPI.h>

#include "Bean.h"
#include "Behavior.h"

BeanSocket::BeanSocket(void) : _radio(9, 10) {
        _pipes[0] = 0xF0F0F0F0E1LL;
        _pipes[1] = 0xF0F0F0F0D2LL;
	_numLines = 0;
        _blinkmAddr = 0x09;
}

BeanSocket::BeanSocket(Bean bean) : _radio(9, 10){
	_bean = bean;
        _pipes[0] = 0xF0F0F0F0E1LL;
        _pipes[1] = 0xF0F0F0F0D2LL;
	_numLines = 0;
        _blinkmAddr = 0x09;
}

void BeanSocket::send(Behavior behavior) {
	_bean.setRolePingOut();
	_radio.stopListening();
	_radio.openWritingPipe(_pipes[0]);
	_radio.openReadingPipe(1, _pipes[1]);

	/* Send header */
	bool ok = _radio.write(&_numLines, sizeof(uint8_t));
	if (ok) {
		Serial.println("Send header ok.");
	}
	else {
		Serial.println("Send header failed.");
	}

	/* Send main script */
	for (int i = 0; i < _numLines; i++) {
		ok = _radio.write(&behavior.getLine(i), sizeof(blinkm_script_line));
		if (ok) {
			Serial.println("Send line ok.");
		}
		else {
			Serial.println("Send line failed. Trying again...");
			i--;
		}
	}
	
	/* Set back as receiver */
	_bean.setRolePongBack();
	_radio.openWritingPipe(_pipes[1]);
	_radio.openReadingPipe(1, _pipes[0]);
	_radio.startListening();
	Serial.println("Send finished.");
}

void BeanSocket::receive() {
	if (!_radio.available()) {
		return;
	}

	/* Check header */
	bool ok = _radio.read(&_numLines, sizeof(uint8_t));
	Serial.print("Got header and will malloc read buffer with # lines: ");
	Serial.println(_numLines);

	/* Read lines */
	bool done = false;
	uint8_t currLine = 0;
	while (!done) {
		if (!_radio.available()) {
			continue; //FIXME: better way of waiting for packets than spinning?
		}
		_radio.read(&READ_BUF[currLine], sizeof(blinkm_script_line));
		currLine++;
		if (currLine >= _numLines) {
			done = true;
		}
	}

	/* Play script */
	BlinkM_writeScript(_blinkmAddr, 0, _numLines, 0, READ_BUF);
	BlinkM_playScript(_blinkmAddr, 0,1,0 );
}

Bean BeanSocket::getBean(void) {
  return _bean;
}


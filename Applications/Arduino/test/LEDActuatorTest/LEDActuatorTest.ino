#include "ArduinoUnit.h"
#include "logger.h"
// assertLess(arg1,arg2)
// assertLessOrEqual(arg1,arg2)
// assertEqual(arg1,arg2)
// assertNotEqual(arg1,arg2)
// assertMoreOrEqual(arg1,arg2)
// assertMore(arg1,arg2)
// Testing timestamped logging suite

// Create test suite
// TestSuite suite;
#define LED_PIN 13
#define MIN 1
#define MAX 0

Logger *logger;
Actuator *led;

void setup() {
  Serial.begin(9600);
}

test(init){
	led = new Actuator(LED_PIN, 0, 255);
	assertEqual(led->bound(MIN), 0);
	assertEqual(led->bound(MAX), 255);
}
test(storage){
	logger = new Logger(100, 0, 1024);
		logger->log(0);delay(100);	
		logger->log(255);delay(100);
		logger->log(0);delay(100);
		logger->log(255);delay(100);
		logger->log(0);delay(100);

	led = new Actuator(LED_PIN, 0, 255);
	led->set(logger->getLog(), logger->length());
	assertEqual(led->length(), 5);
}

void loop() {
  Test::run();
}
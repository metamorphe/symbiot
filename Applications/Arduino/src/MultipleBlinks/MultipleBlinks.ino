/*
 Multiple Blinks

 Demonstrates the use of the Scheduler library for the Arduino Due
 
 Hardware required :
 * LEDs connected to pins 11, 12, and 13

 created 8 Oct 2012
 by Cristian Maglie
 Modified by 
 Scott Fitzgerald 19 Oct 2012
  
 This example code is in the public domain
 
 http://arduino.cc/en/Tutorial/MultipleBlinks

 Modified by Fabrice Oudert 8 Jan 2013 
 https://code.google.com/p/arduino-scoop-cooperative-scheduler-arm-avr/
 
 */

// Include Scheduler since we want to manage multiple tasks.
#include "SchedulerARMAVR.h"

int led1 = LED_BUILTIN; // more portable
int led2 = 12;
int led3 = 11;



// Task no.1: blink LED with 1 second delay.
void loop() {
  Serial.print("LED ");
  Serial.println(led1);
  digitalWrite(led1, HIGH);

  // IMPORTANT:
  // When multiple tasks are running 'delay' passes control to
  // other tasks while waiting and guarantees they get executed.
  Scheduler.delay(1000);

  digitalWrite(led1, LOW);
  Scheduler.delay(1000);
}

// Task no.2: blink LED with 0.1 second delay.
void loop2() {
  Serial.print("LED ");
  Serial.println(led2);
  digitalWrite(led2, HIGH);
  Scheduler.delay(100);
  digitalWrite(led2, LOW);
  Scheduler.delay(100);
}

// Task no.3: accept commands from Serial port
// '0' turns off LED
// '1' turns on LED
void loop3() {
  Serial.print("LED ");
  Serial.println(led3);
  digitalWrite(led3, HIGH);
  Scheduler.delay(100);
  digitalWrite(led3, LOW);
  Scheduler.delay(100);

  // IMPORTANT:
  // We must call 'yield' at a regular basis to pass
  // control to other tasks.
  yield();
}

void setup() {
  Serial.begin(9600);

  // Setup the 3 pins as OUTPUT
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);

  // Add "loop2" and "loop3" to scheduling.
  // "loop" is always started by default.
  Scheduler.startLoop(loop2);
  Scheduler.startLoop(loop3);
}
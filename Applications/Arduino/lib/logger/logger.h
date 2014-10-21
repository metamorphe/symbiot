// Logging interface

#ifndef __Expresso__logger__
#define __Expresso__logger__
#define READY 1
#define OUT_OF_MEMORY 0

#include <Arduino.h>

class Logger {
public:
    Logger(uint16_t);
    void init();
    boolean log(unsigned int);
    void print();
    boolean clear();
    unsigned int* _log;
    unsigned int state;
    unsigned int pos;
private:
	unsigned int size;
	unsigned int max_cap;
	unsigned int min_cap;

 
};

#endif /* defined(__Expresso__logger__) */

// Logging interface

#ifndef __Expresso__logger__
#define __Expresso__logger__
#define READY 1
#define OUT_OF_MEMORY 0

#include <Arduino.h>

class Logger {
public:
    Logger();
    void init();
    boolean log(unsigned int);
    void print();
    boolean clear();
    int _log[20];
    unsigned int state;
private:
	unsigned int size;
	unsigned int max_cap;
	unsigned int min_cap;

    unsigned int pos;
};

#endif /* defined(__Expresso__logger__) */

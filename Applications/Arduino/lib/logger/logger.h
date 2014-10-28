// Logging interface

#ifndef __Expresso__logger__
#define __Expresso__logger__
#define READY 1
#define OUT_OF_MEMORY 0
// #define NULL 0x0000
#include <Arduino.h>

typedef struct {    
    uint16_t value;
    unsigned long timestamp;
    byte priority;
}Record;
typedef struct {    
    Record* curr;
    Record* next;
    unsigned long diff;
}InterruptRecord;

class Logger {
public:
    Logger(uint16_t, uint16_t, uint16_t);
    void init();
    boolean log(uint16_t);/* 16-bit aesthetic */
    void print();
    boolean clear();
    
    unsigned int state;
    uint16_t pos;

    inline Record* length(){return pos;}
    inline Record* getLog(){return _log();}
    inline Record* get(uint16_t _i){ return &(_log[_i]);}
    inline Record* first(){ return &(_log[0]);}
    inline Record* last(){ return &(_log[pos-1]);}
    inline InterruptRecord getIR(uint16_t _i){
        InterruptRecord ir;
        ir.curr = get(_i);
        if(_i + 1 < size) ir.next = get(_i + 1);
        else ir.next = NULL;
        return ir;
    }
    boolean write(char*);
    boolean read(char*);
    
private:
    uint16_t size;
	unsigned int max_cap;
	unsigned int min_cap;
    Record* _log;

};

#endif /* defined(__Expresso__logger__) */

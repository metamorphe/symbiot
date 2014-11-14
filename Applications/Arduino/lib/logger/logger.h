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
    uint16_t curr;
    uint16_t next;
    unsigned long delay;
}InterruptRecord;

class Logger {
public:
    Logger(uint16_t, uint16_t, uint16_t);
    void init();
    boolean log(uint16_t);/* 16-bit aesthetic */
    boolean log(uint16_t, unsigned long timestamp);/* 16-bit aesthetic */
    void printIR();
    void print();
    boolean clear();
    
    unsigned int state;
    uint16_t pos;

    inline uint16_t length(){return pos;}
    inline Record* getLog(){return _log;}
    inline Record* get(uint16_t _i){ return &(_log[_i]);}
    inline Record* first(){ return &(_log[0]);}
    inline Record* last(){ return &(_log[pos-1]);}
    inline InterruptRecord getIR(uint16_t _i){
        InterruptRecord ir;
        Record* curr = get(_i);
        ir.curr = curr->value;
        if(_i < pos - 1){
            Record* next = get(_i + 1);
            ir.next = next->value;
            ir.delay = (next->timestamp - curr->timestamp) / 1000;
        }
        else{
            ir.next = 0;
            ir.delay = 0;
        }
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

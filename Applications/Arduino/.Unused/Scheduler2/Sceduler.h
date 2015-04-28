#ifndef __Expresso__scheduler__
#define __Expresso__scheduler__

#include "string.h"
#include <Arduino.h>
#include "QueueList.h"


class Scheduler{
	public:
		void init(){
			d0 = micros();
		}
		void process(){
			for(short i=0; i < act_length; i++)
		}
		void quanta(){
			dt = micros() - d0;

			if(queue.empty()) return;


			if(todo->timestamp >= dt){
				active->actuate(todo->value);
				todo = queue.pop();
				error += (todo->timestamp - dt);
			}	
		};
		void end()
		
	private:
		unsigned long d0;
		unsigned long dt;
		Record todo; 
		Actuator* active;
		Actuator* act_list;
		short act_length;
		QueueList<Record*> queue;
		unsigned long error;
};
#endif /* defined(__Expresso__scheduler__) */
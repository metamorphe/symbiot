# job.py

class Job(object):
    def __init__(self, b_id, f_id, priority, value, addr):
        self.priority = priority
        self.value = value
        self.behavior_id = b_id
        self.flavor_id = f_id
        self.addr = addr
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)
    def __str__(self):
    	return "{:1.0f}".format(self.addr) + ":" + "{:3.0f}".format(self.value)
    def __sub__(self, other):
    	return abs(self.priority - other.priority)
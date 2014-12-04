# job.py

class Job(object):
    def __init__(self, metadata, priority, value):
        self.priority = priority
        self.value = value
        self.metadata = metadata
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)
    def __str__(self):
    	return "@{:3.2f} ".format(self.priority) + "to {:1.0f}".format(self.metadata.addr) + ":" + "{:3.0f}".format(self.value)
    def __sub__(self, other):
    	return abs(self.priority - other.priority)
from bunch import Bunch
import numpy as np
# job.py
class Job(object):
    def __init__(self, metadata, priority, value, prev = None):
        self.priority = priority
        mc = Bunch()
        for k in metadata:
            mc[k] = metadata[k]
        self.metadata = mc
        self.value = value
        self.prev = prev
        return

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)
    def __str__(self):
        # JOB: DEADLINE: X, LOCALITY: X, HARDNESS: X, VALUE: X
        return ("0x{:02x} ".format(self.metadata.addr) + 
                "|| p {:3.2f} ".format(self.priority) + 
                "|t(ms): {:4.0f} ".format(self.metadata.time * 1000) +   
                "|l: {:2.0f} ".format(self.metadata.locality) +  
                "|h: {:3.0f} ".format(self.metadata.hardness) +  
                "|v: {:3.0f} ".format(self.value)) + hex(id(self.prev))

    	# return "@{:3.2f} ".format(self.priority) + "to {:1.0f}".format(self.metadata.addr) + ":" + "{:3.0f}".format(self.value)
    def __sub__(self, other):
    	return abs(self.metadata.time - other.metadata.time)

    def set_priority(self, type, param = None):
        if type == "edf":
            self.edf()
        if type == "pdf":
            self.pdf()
        if type == "cbs":
            self.cbs(param)
        return self

    def longer(self, s):
        self.metadata.time *= s

    def cbs(self, T):
        self.priority = np.floor(self.metadata.time / T) # 0.010 / 1  ==> 0  1.00001/ 1 ===> 1
        return self

    def edf(self):
        self.priority = self.metadata.time # 0.010 / 1  ==> 0  1.00001/ 1 ===> 1
        return self

    def pdf(self):
        # AVOID divide by 0 errors, priority crashing
        locality =  self.metadata.locality + 1
        hardness = self.metadata.hardness + 1

        self.priority = (   1   * (1 - (1./ locality)) 
                          + 10   * (1./  hardness)
                          + 1000 *  self.metadata.time 
                        )
        return self
from bunch import Bunch
import numpy as np
# job.py
class Job(object):
    def __init__(self, metadata, priority, value):
        self.priority = priority
        mc = Bunch()
        for k in metadata:
            mc[k] = metadata[k]
        self.metadata = mc
        self.value = value

        return

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)
    def __str__(self):
        # JOB: DEADLINE: X, LOCALITY: X, HARDNESS: X, VALUE: X
        return ("addr: 0x{:02x} ".format(self.metadata.addr) + 
                "|t(ms): {:4.0f} ".format(self.metadata.time * 1000) +   
                "|l: {:2.0f} ".format(self.metadata.locality) +  
                "|h: {:3.0f} ".format(self.metadata.hardness)+
                "|v: {:6.2f} ".format(self.value)+
                "|| pr {:6.2f} ".format(self.priority))  

    	# return "@{:3.2f} ".format(self.priority) + "to {:1.0f}".format(self.metadata.addr) + ":" + "{:3.0f}".format(self.value)
    def __sub__(self, other):
    	return abs(self.metadata.time - other.metadata.time)
    
    def dv(self, other):
        return float(other.value - self.value) 

    def tween(self, other, segments, pos, T):
        # linear interpolation
        # print self
        # print other
        # d_t = abs(np.floor(self.metadata.time / T) - np.floor(other.metadata.time / T))

        d_t = (pos + abs(np.floor(self.metadata.time / T))) * T
        # print "d_t", d_t,
        # before = 0, now = 100, = (100  - 0) -100 pos = -1 ==> -100
        # before = 100, now = 0, = (0 - 100) 100 pos = -1 ==> 100

        # now = 0, after = 100, (0 - 100) 100 pos = 1 ==> 100
        # now = 100, after = 0, (100 - 0) -100  pos = 1 ==> -100

        d_v = self.dv(other)
        # print "d_v", d_v
        d_v /= segments
        # print "d_energy", d_v

        # 1000 - 0


        # print "v", d_v, 
       
        # d_v *= pos

        # print "final", d_t, d_v, "vars", segments, pos,
        # print "place", np.floor(d_t / 0.004624)
        self.metadata.time = d_t
        self.value += d_v
        # print self, '\n'
       
        return self


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
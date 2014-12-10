from bunch import Bunch
import numpy as np
# job.py
class Job(object):
    def __init__(self, metadata, priority, value):
        self.priority = priority
        mc = Bunch()
        for k in metadata:
            mc[k] = metadata[k]
        mc.hardhit = False
        self.metadata = mc
        self.value = value

        return

    def clone(self):
        return Job(self.metadata, self.priority, self.value)

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

    def q_str(self, T):

        tween = "TWEENED" if not self.metadata.hardhit else "HARDHIT"
        # JOB: DEADLINE: X, LOCALITY: X, HARDNESS: X, VALUE: X
        return (tween + "|| q:  {:3.0f} ".format(np.floor(self.metadata.time / T)) + 
                "addr: 0x{:02x} ".format(self.metadata.addr) + 
                "|t(ms): {:4.0f} ".format(self.metadata.time * 1000) +   
                "|v: {:6.2f} ".format(self.value))  
    	# return "@{:3.2f} ".format(self.priority) + "to {:1.0f}".format(self.metadata.addr) + ":" + "{:3.0f}".format(self.value)
    def __sub__(self, other):
    	return abs(self.metadata.time - other.metadata.time)
    
    def dv(self, other):
        o = other.value
        s = self.value

        o = (o / self.metadata.k) **  self.metadata.alpha
        s = (s / self.metadata.k) **  self.metadata.alpha
        # CONVERT INTO PERCEPTUAL SPACE

        return float(o - s) 

    def tween(self, other, segments, pos, T, clone):
        # linear interpolation
        # print "DEAD JOB", self.q_str(T)
        # print "NEIG JOB", other.q_str(T)
        d_t = pos + abs(np.floor(self.metadata.time / T))
        # print "d_t", d_t
        d_t *=  T
      
        d_v = self.dv(other)
        d_v /= segments



        # convert in intensity space
        p = (self.value / self.metadata.k) **  self.metadata.alpha
        p += d_v
        I = int( (p ** (1 / self.metadata.alpha)) * self.metadata.k)

      
        if clone:
            j = self.clone()
            # print "CLONE   ", j.q_str(T)
            j.metadata.time = d_t
            j.value = I
            # print "CLONE'   ", j.q_str(T)   
            return j
        else:
            other.metadata.time = d_t
            other.value = I
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
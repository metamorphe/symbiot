"""
manifold.py

A library for compacting actuator instructions.

Example usage:

a = Actuator.linear() # default linear actuator
values = [0, 0, 1, 2, 3, 4, 5, 4, 3, 3, 3]
command = a.get_commands(values)
>>> command
[(0, 0.5), (1, 1), (7, 0), (9, 0.5)]

a = Actuator.linear(10) # actuator that can change at 10 units per ms
values = [0, 10, 15, 20, 10, 0]
command = a.get_commands(values)
>>> command
[(0, 1), (1, 0.75), (3, 0)]
"""



from __future__ import division # use python3 style division
import sys, json
import numpy as np

class Actuator(object):
    """Actuator is a representation of an actuator's physical characteristics
    """
    def __init__(self, dh, dl, alpha = 1.0):
        """ Deltas are 256 long tuples of an actuator's ability to change intensity,
        in units of output per millisecond
        """
        self.delta_high = tuple(dh) # actuator's ability to increase intensity
        self.delta_low = tuple(dl) # actuator's ability to decrease intensity
        self.alpha = alpha # actuator's alpha on Steven's power curve

    @staticmethod
    def linear(speed = 1):
        """ Returns a linear actuator."""
        dh = (speed,) * 256
        dl = (-speed,) * 256
        return Actuator(dh, dl)

    def calc_strength(self, current_output, desired_delta):
        """ calculates the strength that should be output
        """
        current_output = int(current_output)
        delta_high = self.delta_high[current_output]
        delta_low = self.delta_low[current_output]
        if desired_delta > delta_high:
            print "desired delta too high for actuator!"
            return 1.0
        if desired_delta < delta_low:
            print "desired delta too low for actuator!"
            return 0.0
        return (desired_delta - delta_low) / (delta_high - delta_low)

    def adjust_software_impedance(self, commands):
        """ adjusts commands to software delays
        """
        return commands, 1

    def adjust_mechanical_impedance(self, commands):
        """ adjusts commands to mechanical magnitudes
        """
        commands = []
        current_strength = 0
        current_output = cv[0][1]
        for i in xrange(len(cv) - 1): # iterate through each difference
            cmd_pair = (cv[i], cv[i + 1])
            current_time = cmd_pair[0][0]
            d_time = cmd_pair[1][0] - cmd_pair[0][0]
            d_value = cmd_pair[1][1] - current_output
            desired_delta = d_time / d_value
            strength = self.calc_strength(current_output, desired_delta)
            if abs(strength - current_strength) > 0.000001:
                commands.append((current_time, strength))
                current_strength = strength
        return commands

    def perceptual_to_physical(self, commands):
        """ adjusts commands to physical magnitudes
        """
        # scaling factor for regularization
        scaling_factor = 255 / (255 ** (1 / self.alpha))
        def apply_stevens_power_law(cmd):
            if cmd[1]:
                return (cmd[0], int( (cmd[1] ** (1 / self.alpha)) * scaling_factor))
            else:
                return cmd
        return map(apply_stevens_power_law, commands), 1

    def get_commands(self, values):
        # FIRST, GET VALUES INTO SPARSE FORMAT
        commands, sparse_ratio = compact(values)
        # THEN, CORRECT FOR THE SMP PROFILE
        commands, perp_ratio = self.perceptual_to_physical(commands)
        # commands, mech_ratio = self.adjust_mechanical_impedance(commands)
        commands, sft_ratio = self.adjust_software_impedance(commands)

        compression_ratio = len(commands) / len(values)
        return commands, compression_ratio

def compact(values):
    """compact takes an array of integer values and expresses them as a series of
    (time, value) instructions
    e.g. [10, 10, 10, 10, 10, 50, 10, 10, 10] -> [(0, 10), (5, 50), (6, 10), (9, 10)]
    """
    compacted = []
    # remove extraneous values
    prev = None
    for i, v in enumerate(values):
        if v != prev:
            prev = v
            compacted.append((i, v))
    # add end, needed for looping values
    compacted.append((len(values), None))
    return compacted, len(compacted) / len(values)

def main():
    if len(sys.argv) == 1:
        print 'this is manifold.py'
        return
    if sys.argv[1] == 'compact':
        result = compact(json.loads(sys.argv[2]))
        print(json.dumps(result[0])),
        return

if __name__ == '__main__':
    main()





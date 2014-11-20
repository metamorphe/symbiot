import manifold as m
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.simple = [10, 10, 10, 10, 10, 50, 10, 10, 10]
        self.simple_edge = [10, 10, 10, 10, 10, 50, 10]
        self.alternate_on_and_off = [0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.19335375,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.09492187500000002,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005,0.19335375000000005]

    def test_compact_simple(self):
        """ Test simple sparse format compression
        """
        led = m.Actuator.linear()
        commands, compression = led.get_commands(self.simple)
        # COMPRESSION CHECK
        self.assertAlmostEqual(compression, 4.0/len(self.simple))
        # TIME CORRESPONDENCE
        verbose = to_verbose(commands)
        self.assertEqual(verbose, self.simple)

    def test_compact_simple_edge(self):
        led = m.Actuator.linear()
        commands, compression = led.get_commands(self.simple_edge)
        # COMPRESSION CHECK
        self.assertAlmostEqual(compression, 4.0/len(self.simple_edge))
        # TIME CORRESPONDENCE
        verbose = to_verbose(commands)
        self.assertEqual(verbose, self.simple_edge)

    def test_compact_simple_edge_with_alpha(self):
        led = m.Actuator.linear()
        led.alpha = alpha = 1.5
        commands, compression = led.get_commands(self.simple_edge)
        # TIME CORRESPONDENCE
        verbose = to_verbose(commands)
        self.assertEqual(verbose, map(lambda x: int(x ** (1 / alpha)), self.simple_edge))

    def test_compact_complex(self):
        """ Test complex sparse format compression 
        """
        led = m.Actuator.linear()
        commands, compression = led.get_commands(self.alternate_on_and_off)
        
        # TIME CORRESPONDENCE
        verbose = to_verbose(commands)
        # print commands
        self.assertEqual(len(verbose), len(self.alternate_on_and_off))


def to_verbose(values):
    verbose_form = []
    for i, c in enumerate(values):
        t, v = c
        
        if i < len(values)-1:
            time_diff = values[i+1][0] - t
            verbose_form.append((v,) * int(time_diff))
    verbose_form = [x for xs in verbose_form for x in xs]
    return verbose_form
# if __name__ == '__main__':
#     unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=1).run(suite)
import sys
sys.path.append('lib')
import expresso_api as api
import scheduler
import unittest
from  microtest import *
from microbenchmark import get_tests

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.tests = get_tests(None)
        self.pulse = api.get_commands(16, alpha = 0.5)
        self.square = api.get_commands(5, alpha = 0.5)
        pass

    def test_hardness(self):
        np.set_printoptions(suppress=True)
        # print harden(self.pulse)
        print harden(self.square)

    # def test_compact_simple(self):
    #     """ Test simple sparse format compression
    #     """
    #     for t in self.tests:
    #         print t
    #         schedule = t.get_sequence()
    #         edf_schedule = scheduler.to_commands(schedule, "edf")
    #         print "EDF"
    #         for job in edf_schedule:
    #             print job
    #         pdf_schedule = scheduler.to_commands(schedule, "pdf")
    #         print "PDF"
    #         for job in pdf_schedule:
    #             print job


# if __name__ == '__main__':
#     unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=1).run(suite)
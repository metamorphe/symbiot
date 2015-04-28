import sys
sys.path.append('lib')
import expresso_api as api
import scheduler, operator
import unittest
from  microtest import *
from microbenchmark import get_tests
from quanta import Quanta
class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.tests = get_tests(None)
        self.pulse = api.get_commands(16, alpha = 0.5)
        self.square = api.get_commands(5, alpha = 0.5)
        self.candle = api.get_commands(7, alpha = 0.5)
        # pass

    # def test_hardness(self):
    #     np.set_printoptions(suppress=True)
    #     print harden(self.pulse, 0.5, 0.00392156862745098)
    #     # print harden(self.square)
        # harden(self.candle)

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

    # def test_histogram(self):
    #     for t in self.tests:
    #         print t
    #         schedule = t.get_sequence()
    #         print scheduler.histogram(schedule)
    # def test_cbs(self):
    #     for t in self.tests:
    #         print t
    #         schedule = t.get_sequence()
    #         Us, Qs, Ts, timescale = scheduler.calculate_edf_cbs(schedule, scheduler.atmega328_k)
    #         print Us, Qs, Ts, timescale

            
    #         schedule = scheduler.elongate(schedule, timescale)
    #         # for j in schedule:
    #             # print j
    #         schedule = scheduler.cbs(schedule, Us, Ts)
    #         for j in schedule:
    #             print j
    def test_quanta(self):
        for t in self.tests:
            print t
            schedule = t.get_sequence()
            schedule = scheduler.psf(schedule)
            # Qs = Us * Ts
            # # filter commands and apply dither and resurrect
            # idx = 0

            # schedule = []

            # oversubcribers = []
            # push_to_next = []
            # for n, q in quanta:
            #     inner_quanta = to_commands(q, priority_type = "edf")
            #     # inner_quanta.append(push_to_next)
            #     # print n, len(q)
            #     if len(q) > Qs:
            #         # print "oversubscribed"
            #         # over = len(q) - Qs
            #         # push_to_next.append(inner_quanta[-over:-1])
            #         # inner_quanta = inner_quanta[:-over ]
            #         pass
            #     else:
            #         # print idx, "is utilized", "{:3.2f}%".format(len(q) / Qs * 100) 
            #         pass
            #     idx += 1
            # #   server_chunk = clean_server_chunk(server_chunk, i, Us, k)
            #     schedule.append(inner_quanta)


            # # histogram back to schedule
            
            
            # schedule = sum(schedule, [])

            # return schedule
# if __name__ == '__main__':
#     unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=1).run(suite)
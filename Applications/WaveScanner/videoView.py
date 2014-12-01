import sys
import datetime
import math
from munkres import Munkres
import scanner

h_threshold = 14
cluster_thresh = 10

import scanner


def playVideo(videoName):
    scan = scanner.Scanner(videoName)
    pts = scan.get_wave()
    print pts



def main(argv):
    if len(argv) != 1:
        print 'Please Specify a video file to play.'
    playVideo(argv[0])

if __name__ == "__main__":
    main(sys.argv[1:])
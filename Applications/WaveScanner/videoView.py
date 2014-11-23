import numpy as np
import cv2
import sys
import datetime
import math
import matplotlib.pyplot as plt
from munkres import Munkres
import scanner

h_threshold = 14
cluster_thresh = 10


def cost(A,B):
    return math.floor(math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2))

def playVideo(videoName):
    cap = cv2.VideoCapture(videoName)

    m = Munkres()
    n = 0
    myLines = [[0,0,0],]
    while(cap.isOpened()):
        ret, frame = cap.read()
        if frame == None:
            break
        points = scanner.process_frame(frame)
        myLines.append(points)
        vis = np.concatenate((sliver2, color, sliver), axis=1)

        cv2.imshow('frame', vis)
        cv2.imwrite('frames/sliver'+str(n)+'.jpg', vis)
        n+=1
        # time.sleep(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # plt.hist(range(n), myLines)
    # plt.show
    #sending array over to app
    wave = []
    k = 0
    for linepoint in myLines:
        wave.append(linepoint[2])
        k += 1
        if k == 20:
            break

   
    cap.release()
    cv2.destroyAllWindows()

def main(argv):
    if len(argv) != 1:
        print 'Please Specify a video file to play.'
    playVideo(argv[0])

if __name__ == "__main__":
    main(sys.argv[1:])
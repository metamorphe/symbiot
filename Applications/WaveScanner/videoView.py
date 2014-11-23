import numpy as np
import cv2
import sys
import datetime
import math
import matplotlib.pyplot as plt
from munkres import Munkres
import json
import urllib2

step = 20
h_threshold = 14
cluster_thresh = 10
url = 'http://expresso.cearto.com/api/behaviors'


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
        shape = frame.shape
        sliver = frame[0:shape[0],shape[1]/2:shape[1]/2+step]
        sliver2 = sliver.copy()
        edges = cv2.Canny(sliver,50,150,apertureSize = 3)
        color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        lines = cv2.HoughLines(edges,1,np.pi/180,h_threshold)
        # print len(lines[0])
        cost_matrix = []
        candidatePoints = []
        seen = []
        for rho,theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            mx = (x1+x2)/2
            my = (y1+y2)/2
            i = 0
            broken = False
            while i < (len(seen)):
                point, counts = seen[i]
                if abs(my - point) < cluster_thresh:
                    seen[i] = [(point*counts + my)//(counts+1),counts+1]
                    broken = True
                    break
                i+=1
            if broken:
                continue
            else:
                if x2-x1 == 0:
                    slope = 999
                else:
                    slope = (y2-y1)//(x2-x1)
                candidatePoints.append([mx,my,x1,y1,x2,y2])
                cost_matrix.append([cost([0, myLines[n][0]], [mx,my]), cost([0, myLines[n][1]], [mx,my]) + slope, cost([0, myLines[n][2]], [mx,my])])
                seen.append([my,1])
            # cv2.line(sliver,(x1,y1),(x2,y2),(255,0,0),1)
        # print "cost", cost_matrix
        # print seen
        indexes = m.compute(cost_matrix)
        points = [0,0,0]
        # print indexes
        # if len(indexes) != 3:
            # print len(cost_matrix)
        for row, column in indexes:
            points[column] = candidatePoints[row][1]
            x1 = candidatePoints[row][2]
            y1 = candidatePoints[row][3]
            x2 = candidatePoints[row][4]
            y2 = candidatePoints[row][5]
            cv2.line(sliver,(x1,y1),(x2,y2),(255,0,0),5)
        j = 0
        for value in points:
            if value == 0:                
                points[j] = myLines[n-1][column]
            j+=1
        # print n, points
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

    json_data = json.dumps({
        'behavior': {
        'name': 'TestArray2',
        'notification': 0,
        'active': 0,
        'unable': 0,
        'low_energy': 0,
        'turning_on': 0,
        'states': wave
        }
    })
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    print "Request", req
    print "Data", json_data
    response = urllib2.urlopen(url, json_data)
    cap.release()
    cv2.destroyAllWindows()

def main(argv):
    if len(argv) != 1:
        print 'Please Specify a video file to play.'
    playVideo(argv[0])

if __name__ == "__main__":
    main(sys.argv[1:])
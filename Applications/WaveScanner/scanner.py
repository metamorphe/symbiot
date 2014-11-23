import cv2
from munkres import Munkres
import video
import numpy as np


class Scanner():
    step = 20
    h_threshold = 14
    cluster_thresh = 10


    def __init__(self, videoName):
        self.video = Video().open(videoName)
        self.munkres = Munkres()
        self.heights = []
        self.n = 0

    def segment(self, frame):
        shape = frame.shape
        sliver = frame[0:shape[0],shape[1]/2:shape[1]/2+step]
        sliver2 = sliver.copy()
        edges = cv2.Canny(sliver,50,150,apertureSize = 3)
        color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        return cv2.HoughLines(edges,1,np.pi/180,h_threshold)[0]

    def extract(self, lines):
        cost_matrix = []
        candidatePoints = []
        seen = []
        for rho,theta in lines:
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
                cost_matrix.append([cost([0, self.heights[self.n][0]], [mx,my]), cost([0, self.heights[self.n][1]], [mx,my]) + slope, cost([0, self.heights[self.n][2]], [mx,my])])
                seen.append([my,1])
        indexes = m.compute(cost_matrix)
        points = [0,0,0]
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
                points[j] = self.heights[self.n-1][column]
            j+=1
        return points

    def process_frame(self, frame):
        # print len(lines[0])
        lines = self.segment(frame)
        points = self.extract(lines)
        self.n += 1

    def get_wave(self):
        # return self.heights
        return np.cos(np.linspace(0, 6 *np.pi, 50))
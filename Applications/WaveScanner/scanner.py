import cv2
from munkres import Munkres
import video
import numpy as np
import math


def get_max(array):
    mean = np.mean(array, axis=1)
    var = np.var(array, axis=1)
    waveline = var.index(max(var))
    if waveline = 0:
        return abs(mean[1]-mean[2])*2, waveline
    elif waveline = 1:
        return abs(mean[0]-mean[2])*2, waveline
    else:
        return abs(mean[1]-mean[0])*2, waveline

class Scanner():
    step = 20
    h_threshold = 14
    cluster_thresh = 10


    def __init__(self, videoName):
        self.video = video.Video().open(videoName)
        self.munkres = Munkres()
        self.heights = [[0,0,0]]
        self.n = 0

    def __cost(self, A,B):
        return math.floor(math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2))

    def segment(self, frame):
        return cv2.HoughLines(frame,1,np.pi/180,self.h_threshold)[0]

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
                if abs(my - point) < self.cluster_thresh:
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
                cost_matrix.append([self.__cost([0, self.heights[self.n][0]], [mx,my]),
                                    self.__cost([0, self.heights[self.n][1]], [mx,my]) + slope,
                                    self.__cost([0, self.heights[self.n][2]], [mx,my])])
                seen.append([my,1])
        indexes = self.munkres.compute(cost_matrix)
        points = [0,0,0]
        for row, column in indexes:
            points[column] = candidatePoints[row][1]
            x1 = candidatePoints[row][2]
            y1 = candidatePoints[row][3]
            x2 = candidatePoints[row][4]
            y2 = candidatePoints[row][5]
        j = 0
        # for value in points:
        #     if value == 0:                
        #         points[j] = self.heights[self.n-1][column]
        #     j+=1
        return points

    def process_frame(self, frame):
        # print len(lines[0])
        shape = frame.shape
        sliver = frame[0:shape[0],shape[1]/2:shape[1]/2+self.step]
        edges = cv2.Canny(sliver,50,150,apertureSize = 3)
        return edges

    def get_wave(self):
        while(self.video.isOpened()):
            ret, frame = self.video.query()
            if not ret:
                break;
            canny = self.process_frame(frame)
            lines = self.segment(canny)
            frame_points = self.extract(lines)
            self.heights.append(frame_points)
            self.n += 1
        wave = []
        max_h, waveline = get_max(self.heights)
        for pts in self.heights:
            wave.append(pts[waveline]/max_h)
        return wave
        # return np.cos(np.linspace(0, 6 *np.pi, 50))
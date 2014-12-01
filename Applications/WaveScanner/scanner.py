import cv2
from munkres import Munkres
import video
import numpy as np
import math
from sklearn.cluster import KMeans

def normalize(array):
    # print array
    mean = np.mean(array, axis=0)
    var = np.var(array, axis=0)
    waveline = np.argmax(var)
    for pts in array:
        print pts
    midline = 1
    botline = 2 - (waveline)
    print waveline, botline
    np_arr = np.array(array).T
    return np.divide(np_arr[botline] - np_arr[waveline], 2 * (np_arr[botline] - np_arr[midline]))


class Scanner():
    step = 20
    h_threshold = 14
    cluster_thresh = 10
    mid = 0

    def __init__(self):
        self.munkres = Munkres()
        self.heights = [[0.0,0.0,0.0]]
        self.n = 0

    # def __init__(self, videoName):
    #     self.video = video.Video().open(videoName)
    #     self.munkres = Munkres()
    #     self.heights = [[0.0,0.0,0.0]]
    #     self.n = 0

    def segment(self, frame):
        return cv2.HoughLines(frame,1,np.pi/180,self.h_threshold)

    def extract(self, lines, mid):
        cost_matrix = []
        candidatePoints = []
        seen = []
        km = KMeans(n_clusters=3)
        for rho,theta in lines:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = x0 + 1000*(-b)
            y1 = y0 + 1000*(a)
            x2 = x0 - 1000*(-b)
            y2 = y0 - 1000*(a)
            mx = (x1+x2)/2
            my = (y1+y2)/2
            if x2-x1 == 0:
                slope = 999.9
            else:
                slope = (y2-y1)/(x2-x1)
            candidatePoints.append([mx,my,slope])
        if len(candidatePoints) >= 3:
            km.fit(candidatePoints)
            clusters = km.cluster_centers_
        else:
            clusters = candidatePoints
        for center in clusters:
            mx = center[0]
            my = center[1]
            slope = center[2]
            cost_matrix.append([np.linalg.norm([[0.0, self.heights[self.n][0]], [mx,my]])/4 + slope + my/4 + mid/4,
                                np.linalg.norm([[0.0, self.heights[self.n][1]], [mx,my]])/4 + slope + my/4 + mid/4,
                                np.linalg.norm([[0.0, self.heights[self.n][2]], [mx,my]])/4 + slope + my/4 + mid/4])
        indexes = self.munkres.compute(cost_matrix)
        points = [0.0,0.0,0.0]
        for row, column in indexes:
            points[column] = candidatePoints[row][1]
        j = 0
        for value in points:
            if value == 0:
                max_cnt = 0
                max_pnt = 0
                for point, counts in seen:
                    if counts > max_cnt:
                        max_pnt = point
                points[j] = max_pnt
            j+=1
        return points

    def process_frame(self, frame):
        # print len(lines[0])
        shape = frame.shape
        self.mid = shape[0]/2
        # sliver = frame[0:shape[0],shape[1]/2:shape[1]/2+self.step]
        # edges = cv2.Canny(sliver,50,150,apertureSize = 3)
        edges = cv2.Canny(frame,50,150,apertureSize = 3)
        return edges

    def get_wave(self):
        while(self.video.isOpened()):
            ret, frame = self.video.query()
            if not ret:
                break;
            # print frame.shape
            cv2.imshow('frame', frame)
            canny = self.process_frame(frame)
            lines = self.segment(canny)
            h,w = frame.shape
            frame_points = self.extract(lines, h/2)
            self.heights.append(frame_points)
            self.n += 1
        self.video.close()
        return normalize(self.heights[1:])
        # return np.cos(np.linspace(0, 6 *np.pi, 50))

    def appendPts(self, pts):
        self.heights.append(pts)
        self.n += 1

    def get_heights(self):
        return normalize(self.heights[1:])

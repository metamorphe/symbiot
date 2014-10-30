import numpy as np
import cv2
import sys

step = 20

def playVideo(videoName):
	cap = cv2.VideoCapture(videoName)

	while(cap.isOpened()):
	    ret, frame = cap.read()
	    if frame == None:
	    	break
	    shape = frame.shape
	    sliver = frame[0:shape[0],shape[1]/2:shape[1]/2+step]
	    # frame = frame[shape[0]/2:shape[0]/2+step, 0:shape[1]]
	    # cv2.imshow('frame',frame)
	    # edges = cv2.Canny(sliver,50,150,apertureSize = 3)

	    # lines = cv2.HoughLines(sliver,1,np.pi/180,200)
	    # for rho,theta in lines[0]:
		   #  a = np.cos(theta)
		   #  b = np.sin(theta)
		   #  x0 = a*rho
		   #  y0 = b*rho
		   #  x1 = int(x0 + 1000*(-b))
		   #  y1 = int(y0 + 1000*(a))
		   #  x2 = int(x0 - 1000*(-b))
		   #  y2 = int(y0 - 1000*(a))

		   #  cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

	    cv2.imshow('frame', sliver)


	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

	cap.release()
	cv2.destroyAllWindows()

def main(argv):
	if len(argv) != 1:
		print 'Please Specify a video file to play.'
	playVideo(argv[0])

if __name__ == "__main__":
	main(sys.argv[1:])
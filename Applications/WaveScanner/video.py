import cv2

class Video:
	def open(self, videoName):
		self.cap = cv2.VideoCapture(videoName)
		return self

	def query(self):
		return self.cap.read()

	def isOpened(self):
		return self.cap.isOpened()

	def close(self):
		self.cap.release()
		cv2.destroyAllWindows()
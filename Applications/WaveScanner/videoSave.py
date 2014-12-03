import numpy as np
import cv2
import sys

def videoSave(videoName):
    cap = cv2.VideoCapture(0)

    w=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
    h=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))
    # video recorder
    fourcc = cv2.cv.CV_FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
    out = cv2.VideoWriter(videoName, fourcc, 20.0, (w, h), isColor=False)

    # Define the codec and create VideoWriter object
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter(videoName,fourcc, 20.0, (640,480), isColor=False)

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret==True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # ret,bin = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
            # img = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            #             cv2.THRESH_BINARY,11,2)
            # blur = cv2.bilateralFilter(img,9,75,75)
            ret3,bin = cv2.threshold(gray,1,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            out.write(bin)

            cv2.imshow('frame', bin)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def main(argv):
    print argv
    if len(argv) != 1:
        print 'Please Specify a title to save video as.'
    videoSave(argv[0])

if __name__ == "__main__":
    main(sys.argv[1:])
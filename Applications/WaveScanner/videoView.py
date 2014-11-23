import sys
import scanner

url = 'http://expresso.cearto.com/api/behaviors'

def playVideo(videoName):
    scan = scanner.Scanner(videoName)
    pts = scan.get_wave()
    for pt in pts:
        print pt

    # plt.hist(range(n), myLines)
    # plt.show

    # json_data = json.dumps({
    #     'behavior': {
    #     'name': 'TestArray2',
    #     'notification': 0,
    #     'active': 0,
    #     'unable': 0,
    #     'low_energy': 0,
    #     'turning_on': 0,
    #     'states': wave
    #     }
    # })
    # req = urllib2.Request(url)
    # req.add_header('Content-Type', 'application/json')
    # response = urllib2.urlopen(url, json_data)

def main(argv):
    if len(argv) != 1:
        print 'Please Specify a video file to play.'
    playVideo(argv[0])

if __name__ == "__main__":
    main(sys.argv[1:])
import cv2
def takeSnapshot():
    vco = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = vco.read()
        print(ret)
        cv2.imwrite("newpic.jpg",frame)
        #result = False
    
    vco.release()
    cv2.destroyAllWindows()

takeSnapshot()
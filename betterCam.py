import numpy as np
import cv2

# Open a sample video available in sample-videos
vcap = cv2.VideoCapture('http://192.168.43.1:8080/video')
while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()
    #print cap.isOpened(), ret
    if frame is not None:
        # Display the resulting frame
        cv2.imshow('frame',frame)
        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print ("Frame is None")
        break
        
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

vcap.release()
cv2.destroyAllWindows()

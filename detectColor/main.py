import cv2
import numpy as np
import bgr_hvs 
from PIL import Image

video = cv2.VideoCapture(0)
color_for_track  = [0,255,255]

while True:
    _ , record = video.read()
    frame=cv2.cvtColor(record, cv2.COLOR_BGR2HSV) 
    
    min,max = bgr_hvs.get_limits(color_for_track)   
    
    mask = cv2.inRange(frame, min, max) 
    mask_ = Image.fromarray(mask)
    
    box = mask_.getbbox()   # Searching color coordinates as (x1,y1) , (x2,y2)
    print(box)
    if box  is not None:
            x1, y1, x2, y2 = box
            cv2.rectangle( record, (x1,y1), (x2,y2), (0,255,0), 2)
    
    cv2.imshow("camera", record)
    if  cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
    

video.release()
cv2.destroyAllWindows()
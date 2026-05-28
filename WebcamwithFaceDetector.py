#==================================================================
#  Simple Face Detection
#==================================================================

import cv2

cap = cv2.VideoCapture(0) 
facedetector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True: # while loop for capturing video continuously 
    
    retval,frame = cap.read() # .read gives the frame and the return value of the read function 
    
    if not retval:
        print("Cannot Access The Camera")
        break
    
    # convert to grayscale because its easier to process and faster les computation
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # detect faces 
    faces = facedetector.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    
    #draw rectangle around faces   
    for (x,y,w,h) in faces:  # x,y -. starting point, w,h -> width height
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) # created rectangle around face 
        cv2.putText(frame,"Face_Detected",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    
    cv2.imshow("Face Detection",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
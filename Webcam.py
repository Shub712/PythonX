import cv2

cap = cv2.VideoCapture(0) 

while True: # while loop for capturing video continuously 
    
    retval,frame = cap.read() # .read gives the frame and the return value of the read function 
    
    if retval is True : # if return value is true it shows the frame 

        cv2.imshow("Webcam Feed",frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): # 
            break

cap.realease()
cv2.destroyAllWindows()
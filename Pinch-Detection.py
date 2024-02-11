import cv2 


vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
#declares the variable Ret and Frame and gives both of those Vars the value of vid.read(), which means that they read the incoming video 

    cv2.imshow('frame', frame)
#then it shows the Frame which we declared in the last line, and gives it the name of frame (and since we declared frame as the camera in the last line, it just displays the camera)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#if q key is pressed it stops the while loop which forces the program to go to the next couple lines 

#closes the lines
vid.release()

cv2.destroyAllWindows()
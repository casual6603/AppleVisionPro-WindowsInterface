import numpy as np
import cv2 
import mediapipe as mp


#I guess some of the names in mediapipe are really long so we r shortening them here
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands






vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while vid.isOpened():
        sucess, image = vid.read()
        if not sucess:
            print("Error!")
            break
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
vid.release()














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
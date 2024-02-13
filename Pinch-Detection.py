import numpy as np
import cv2 
import mediapipe as mp
import pyautogui 
import time

#I guess some of the names in mediapipe are really long so we r shortening them here
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands






vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)

x_Index_finger = 0
y_Index_finger = 0
x_thumb = 0
y_thumb = 0
rouneded_x_Index_finger = 0
rouneded_x_thumb = 0
roundeded_y_Index_finger = 0
rouneded_y_thumb = 0
upper_bound_x = 0
lower_bound_x = 1000
upper_bound_y = 0
lower_bound_y = 1000
x = 500
y = 500

with mp_hands.Hands(
    model_complexity=1,
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
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:



                x_Index_finger = hand_landmarks.landmark[8].x  
                y_Index_finger = hand_landmarks.landmark[8].y  
                x_thumb = hand_landmarks.landmark[4].x
                y_thumb = hand_landmarks.landmark[4].y


            rouneded_x_Index_finger = round(x_Index_finger, 4)
            rouneded_x_thumb = round(x_thumb, 4)

            roundeded_y_Index_finger = round(y_Index_finger, 4)
            rouneded_y_thumb = round(y_thumb, 4)
            print(roundeded_y_Index_finger, rouneded_y_thumb)


        upper_bound_x = x_Index_finger * 1.02
        lower_bound_x = x_Index_finger * 0.98
        upper_bound_y = y_Index_finger * 1.1
        lower_bound_y = y_Index_finger * 0.9



        print(upper_bound_y, lower_bound_y)
        if upper_bound_x > rouneded_x_Index_finger and rouneded_x_Index_finger > lower_bound_x and upper_bound_x > rouneded_x_thumb and rouneded_x_thumb > lower_bound_x:
            if upper_bound_y > roundeded_y_Index_finger and roundeded_y_Index_finger > lower_bound_y and upper_bound_y > rouneded_y_thumb and rouneded_y_thumb > lower_bound_y:
                print("yea")
                pyautogui.moveTo(100, 200)   
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
vid.release()















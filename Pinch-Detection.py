import cv2 
import mediapipe as mp
import pyautogui 
import time

#I guess some of the names in mediapipe are really long so we r shortening them here
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands





#create the camera object 
vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)


#variables 
x_Index_finger = 0
y_Index_finger = 0
x_Middle_finger = 0
y_Middle_finger = 0
x_thumb = 0
y_thumb = 0


#rounding the x,y for the fingers

rouneded_x_Index_finger = 0
rouneded_x_thumb = 0
roundeded_y_Index_finger = 0
rouneded_y_thumb = 0
rounded_y_middle_finger = 0
rounded_x_middle_finger = 0


#creating bounds
upper_bound_x_left = 0
lower_bound_x_left = 1000
upper_bound_y_left = 0
lower_bound_y_left = 1000
lower_bound_x_right = 0
upper_bound_x_right = 0
upper_bound_y_right = 0
lower_bound_y_right = 0








last_click_time_left = 0
last_click_time_right = 0


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

                x_Middle_finger = hand_landmarks.landmark[12].x
                y_Middle_finger = hand_landmarks.landmark[12].y




            rouneded_x_Index_finger = round(x_Index_finger, 4)
            rouneded_x_thumb = round(x_thumb, 4)

            roundeded_y_Index_finger = round(y_Index_finger, 4)
            rouneded_y_thumb = round(y_thumb, 4)
            print(roundeded_y_Index_finger, rouneded_y_thumb)

            rounded_x_middle_finger = round(x_Middle_finger, 4)
            rounded_y_middle_finger = round(y_Middle_finger, 4)

            print(rounded_x_middle_finger, rounded_y_middle_finger)


   
        #creating bounds for finger detection
        upper_bound_x = x_Index_finger * 1.02
        lower_bound_x = x_Index_finger * 0.98
        upper_bound_y = y_Index_finger * 1.1
        lower_bound_y = y_Index_finger * 0.9


        upper_bound_x_right = x_Middle_finger * 1.03
        lower_bound_x_right = x_Middle_finger * 0.97
        upper_bound_y_right = y_Middle_finger * 1.05 
        lower_bound_y_right = y_Middle_finger * 0.95




#left click support
        print(upper_bound_y, lower_bound_y)
        if upper_bound_x > rouneded_x_Index_finger and rouneded_x_Index_finger > lower_bound_x and upper_bound_x > rouneded_x_thumb and rouneded_x_thumb > lower_bound_x:
            if upper_bound_y > roundeded_y_Index_finger and roundeded_y_Index_finger > lower_bound_y and upper_bound_y > rouneded_y_thumb and rouneded_y_thumb > lower_bound_y:
                current_time = time.time()
                if current_time - last_click_time_left > 0.5:  # Check if 2 seconds have passed since the last click
                    print("L")
                    pyautogui.click()
                    last_click_time_left = current_time  # Update the last click time

#right click support 
        if upper_bound_x_right > rounded_x_middle_finger and rounded_x_middle_finger > lower_bound_x_right and upper_bound_x_right > rouneded_x_thumb and rouneded_x_thumb > lower_bound_x_right:
            if upper_bound_y_right > rounded_y_middle_finger and rounded_y_middle_finger > lower_bound_y_right and upper_bound_y_right > rouneded_y_thumb and rouneded_y_thumb > lower_bound_y_right:
                current_time_right = time.time()
                if current_time_right - last_click_time_right > 0.5:  # Check if 2 seconds have passed since the last click
                    print("Right Click Detected")
                    pyautogui.click(button='right')  # right-click the mouse
                    last_click_time_right = current_time_right  # Update the last click time


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
vid.release()















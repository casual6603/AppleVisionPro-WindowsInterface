import cv2
import mediapipe as mp
import pyautogui
import time

# I guess some of the names in mediapipe are really long so we r shortening them here
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# create the camera object
vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)

# variables
x_Index_finger = 0
y_Index_finger = 0
x_Middle_finger = 0
y_Middle_finger = 0
x_ring_finger = 0
y_ring_finger = 0
x_thumb = 0
y_thumb = 0

# rounding the x,y for the fingers

rouneded_x_Index_finger = 0
rouneded_x_thumb = 0
roundeded_y_Index_finger = 0
rouneded_y_thumb = 0
rounded_y_middle_finger = 0
rounded_x_middle_finger = 0
rounded_x_ring_finger = 0
rounded_y_ring_finger = 0

# creating bounds
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

                x_ring_finger = hand_landmarks.landmark[16].x
                y_ring_finger = hand_landmarks.landmark[16].y

            rouneded_x_Index_finger = round(x_Index_finger, 4)
            rouneded_x_thumb = round(x_thumb, 4)

            roundeded_y_Index_finger = round(y_Index_finger, 4)
            rouneded_y_thumb = round(y_thumb, 4)

            rounded_x_middle_finger = round(x_Middle_finger, 4)
            rounded_y_middle_finger = round(y_Middle_finger, 4)

            rounded_x_ring_finger = round(x_ring_finger, 4)
            rounded_y_ring_finger = round(y_ring_finger, 4)


        # creating bounds for finger detection
        upper_bound_x = x_Index_finger * 1.02
        lower_bound_x = x_Index_finger * 0.98
        upper_bound_y = y_Index_finger * 1.1
        lower_bound_y = y_Index_finger * 0.9

        upper_bound_x_right = x_Middle_finger * 1.03
        lower_bound_x_right = x_Middle_finger * 0.97
        upper_bound_y_right = y_Middle_finger * 1.05
        lower_bound_y_right = y_Middle_finger * 0.95

        upper_bound_x_ring = x_ring_finger * 1.05
        lower_bound_x_ring = x_ring_finger * 0.95
        upper_bound_y_ring = y_ring_finger * 1.05
        lower_bound_y_ring = y_ring_finger * 0.95

        # left click support with index finger and thumb pinch
        if upper_bound_x > rouneded_x_Index_finger and rouneded_x_Index_finger > lower_bound_x and upper_bound_x > rouneded_x_thumb and rouneded_x_thumb > lower_bound_x:
            if upper_bound_y > roundeded_y_Index_finger and roundeded_y_Index_finger > lower_bound_y and upper_bound_y > rouneded_y_thumb and rouneded_y_thumb > lower_bound_y:
                current_time = time.time()
                if current_time - last_click_time_left > 0.1:  # Check if 2 seconds have passed since the last click
                    print("Left Click Detected")
                    pyautogui.click()
                    last_click_time_left = current_time  # Update the last click time

        # right click support with middle finger and thumb pinch
        if upper_bound_x_right > rounded_x_middle_finger and rounded_x_middle_finger > lower_bound_x_right and upper_bound_x_right > rouneded_x_thumb and rouneded_x_thumb > lower_bound_x_right:
            if upper_bound_y_right > rounded_y_middle_finger and rounded_y_middle_finger > lower_bound_y_right and upper_bound_y_right > rouneded_y_thumb and rouneded_y_thumb > lower_bound_y_right:
                current_time_right = time.time()
                if current_time_right - last_click_time_right > 0.1:  # Check if 2 seconds have passed since the last click
                    print("Right Click Detected")
                    pyautogui.click(button='right')  # right-click the mouse
                    last_click_time_right = current_time_right  # Update the last click time

        # drag with ring finger and thumb pinch
        
        hand_last_moved_time = time.time()  # Initialize last moved time

        while True:
            # Update your variables here

            if not (upper_bound_x_ring > rounded_x_ring_finger and rounded_x_ring_finger > lower_bound_x_ring and upper_bound_x_ring > rouneded_x_thumb and rouneded_x_thumb > lower_bound_x_ring):
                break

            if not (upper_bound_y_ring > rounded_y_ring_finger and rounded_y_ring_finger > lower_bound_y_ring and upper_bound_y_ring > rouneded_y_thumb and rouneded_y_thumb > lower_bound_y_ring):
                break
            print('Hand moving')
            current_time = time.time()
            elapsed_time = current_time - hand_last_moved_time


            starting_x_mouse,  starting_y_mouse = pyautogui.position()

            if elapsed_time > 1 and starting_x == rounded_x_ring_finger:  
                print(starting_x, rounded_x_ring_finger)
                print("Hand not moving, exiting loop")
                break


            change_in_x = starting_x - rounded_x_ring_finger
            change_in_y = starting_y - rounded_y_ring_finger
            screen_x = change_in_x * 1920
            screen_y = change_in_y * 1080
            final_screen_x = starting_x_mouse + screen_x
            final_screen_y = starting_y_mouse + screen_y
            print(f"X: {final_screen_x}, Y: {final_screen_y}")
            pyautogui.moveTo(final_screen_x, final_screen_y)




        #so i have to take the posiiton where the pinch was found which is in the var starting x and starting y. Then i have to continually calculate the change in the x and the y, then convert that change into screen pixels by multiplying the value by 1920 (for x) and 1080 (for y)





                # Click and Drag Support
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    vid.release()

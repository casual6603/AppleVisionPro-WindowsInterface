import cv2
import mediapipe as mp

def main():
       cap = cv2.VideoCapture(0)
       
       mp_drawing = mp.solutions.drawing_utils
       mp_hands = mp.solutions.hands
       
       with mp_hands.Hands(
              static_image_mode=False,
              max_num_hands=1,
              min_detection_confidence=0.5) as hands:
              
              while cap.isOpened():
                     success, image = cap.read()
                     if not success:
                            print("Failed to read video")
                            break
                     
                     image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                     image.flags.writeable = False
                     results = hands.process(image)
                     
                     image.flags.writeable = True
                     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                     
                     if results.multi_hand_landmarks:
                            for hand_landmarks in results.multi_hand_landmarks:
                                   x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                                   y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                                   print(f"X: {x}, Y: {y}")
                                   
                                   mp_drawing.draw_landmarks(
                                          image,
                                          hand_landmarks,
                                          mp_hands.HAND_CONNECTIONS)
                     
                     cv2.imshow('Hand Tracking', image)
                     
                     if cv2.waitKey(5) & 0xFF == 27:
                            break
       
       cap.release()
       cv2.destroyAllWindows()

if __name__ == "__main__":
       main()
import cv2
import mediapipe as mp
# To capture the video
cap = cv2.VideoCapture(0)

hand_detector = mp.solutions.hands.Hands() # to detect hand
drawing_utils =  mp.solutions.drawing_utils # to draw
while 1:
    _, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks # coordinates of hand landmarks
    # print(hands)
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand) # draw where hand was detected

    cv2.imshow('Air Draw', frame)
    cv2.waitKey(1)



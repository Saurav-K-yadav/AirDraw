import cv2
import mediapipe as mp
import pyautogui
# To capture the video
cap = cv2.VideoCapture(0)

hand_detector = mp.solutions.hands.Hands() # to detect hand
drawing_utils = mp.solutions.drawing_utils  # to draw
screen_width, screen_height = pyautogui.size()
index_y = 0
while 1:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)  # make left top as (0,0)
    frame_height, frame_width, _ = frame.shape  # get height, width of frame where image is captured
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks  # coordinates of hand landmarks
    # print(hands)
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)  # draw where hand was detected
            landmarks = hand.landmark
            for ids, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)  # making with respect to frame
                y = int(landmark.y * frame_height)
                print(x, y)
                if ids == 8:  # id of index finger's tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(127, 255, 0))  # draw a circle
                    index_x = screen_width/frame_width*x  # scaling the width
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)  # to move the cursor
                if ids == 4:  # id of thumb finger's tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(127, 255, 0))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    if abs(index_y - thumb_y < 15):  # if thumb and index come together then click
                        pyautogui.click()  # click
                        pyautogui.sleep(2)
                        print('clicked')

    cv2.imshow('Air Draw', frame)
    cv2.waitKey(1)



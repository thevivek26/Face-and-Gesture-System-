import cv2
import numpy as np
import mediapipe as mp


class GestureRecognition:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        # MediaPipe modules
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        self.hands = mp.solutions.hands.Hands(max_num_hands=1)
        self.drawer = mp.solutions.drawing_utils

    # -------- FACE EMOTION (Simple Rule Based) --------
    def detect_emotion(self, landmarks, h, w):
        top_lip = landmarks[13]
        bottom_lip = landmarks[14]
        left_mouth = landmarks[61]
        right_mouth = landmarks[291]

        mouth_open = abs(top_lip.y - bottom_lip.y) * h
        mouth_width = abs(left_mouth.x - right_mouth.x) * w

        if mouth_open > 18 and mouth_width > 60:
            return "Happy"
        elif mouth_open < 8:
            return "Angry"
        else:
            return "Sad"

    # -------- HAND GESTURE --------
    def detect_hand(self, hand):
        tips = [4, 8, 12, 16, 20]
        fingers = []

        fingers.append(hand.landmark[tips[0]].x < hand.landmark[tips[0] - 1].x)

        for i in range(1, 5):
            fingers.append(hand.landmark[tips[i]].y < hand.landmark[tips[i] - 2].y)

        if fingers == [False, True, True, False, False]:
            return "Peace ✌"
        elif fingers == [True, True, True, True, True]:
            return "Open Hand 🖐"
        elif fingers == [False, False, False, False, False]:
            return "Fist ✊"
        elif fingers == [False, True, False, False, False]:
            return "One ☝"
        else:
            return "Gesture"

    # -------- START CAMERA --------
    def start(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, _ = frame.shape

            # Face
            face_result = self.face_mesh.process(rgb)
            if face_result.multi_face_landmarks:
                for face in face_result.multi_face_landmarks:
                    emotion = self.detect_emotion(face.landmark, h, w)
                    cv2.putText(frame, f"Emotion: {emotion}", (30, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Hand
            hand_result = self.hands.process(rgb)
            if hand_result.multi_hand_landmarks:
                for hand in hand_result.multi_hand_landmarks:
                    self.drawer.draw_landmarks(
                        frame, hand, mp.solutions.hands.HAND_CONNECTIONS
                    )
                    gesture = self.detect_hand(hand)
                    cv2.putText(frame, f"Hand: {gesture}", (30, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            cv2.imshow("Gesture & Emotion Recognition", frame)

            if cv2.waitKey(1) == 13:  # ENTER
                break

        self.cap.release()
        cv2.destroyAllWindows()

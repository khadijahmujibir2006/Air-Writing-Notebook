import cv2
import mediapipe as mp


class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hand(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        return img

    def get_landmarks(self, img):
        landmarks = []
        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    img, hand, self.mp_hands.HAND_CONNECTIONS
                )
                for lm in hand.landmark:
                    h, w, _ = img.shape
                    landmarks.append((int(lm.x * w), int(lm.y * h)))
        return landmarks

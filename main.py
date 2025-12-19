import cv2
from hand_tracking import HandTracker
from gestures import fingers_up
from canvas import Canvas
from save_utils import save_image


cap = cv2.VideoCapture(0)
tracker = HandTracker()
canvas = Canvas()

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)

    tracker.find_hand(frame)
    landmarks = tracker.get_landmarks(frame)

    if landmarks:
        finger_state = fingers_up(landmarks)

        # ---------------- COLOR GESTURES ----------------
        if finger_state == [1, 0, 0, 0, 0]:
            canvas.color = (0, 0, 255)     # Red (Thumb)

        elif finger_state == [0, 1, 1, 0, 0]:
            canvas.color = (0, 255, 0)     # Green (Index + Middle)

        elif finger_state == [0, 1, 0, 0, 1]:
            canvas.color = (255, 0, 0)     # Blue (Index + Pinky)

        elif finger_state == [1, 1, 1, 1, 1]:
            canvas.color = (255, 0, 255)   # Pink (All fingers)

        # ---------------- DRAW ----------------
        if finger_state[1] and not finger_state[2]:
            x, y = landmarks[8]
            canvas.draw(x, y)
        else:
            canvas.prev_x = 0
            canvas.prev_y = 0

        # ---------------- UNDO / REDO ----------------
        if sum(finger_state) == 0:
            canvas.undo()

        if sum(finger_state) == 5:
            canvas.redo()

        # ---------------- CLEAR ----------------
        if finger_state[1] and finger_state[2]:
            canvas.clear()

    frame = cv2.addWeighted(frame, 0.5, canvas.canvas, 0.5, 0)
    cv2.imshow("Air Writing Notebook", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        save_image(canvas.canvas)
        break

cap.release()
cv2.destroyAllWindows()

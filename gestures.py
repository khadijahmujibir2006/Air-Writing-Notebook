def fingers_up(landmarks):
    if not landmarks:
        return [0, 0, 0, 0, 0]

    fingers = []

    # Thumb
    fingers.append(1 if landmarks[4][0] > landmarks[3][0] else 0)

    # Other fingers
    tips = [8, 12, 16, 20]
    for tip in tips:
        fingers.append(1 if landmarks[tip][1] < landmarks[tip - 2][1] else 0)

    return fingers

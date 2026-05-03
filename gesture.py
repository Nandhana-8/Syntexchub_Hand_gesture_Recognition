import mediapipe as mp

def detect_gesture(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for tip in tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    # Gesture conditions
    if fingers == [0, 0, 0, 0, 0]:
        return "Pause ⏸"
    elif fingers == [1, 1, 1, 1, 1]:
        return "Play ▶"
    elif fingers == [1, 0, 0, 0, 0]:
        return "Like 👍"
    elif fingers == [0, 1, 0, 0, 0]:
        return "Volume Up 🔊"
    elif fingers == [0, 0, 0, 0, 1]:
        return "Volume Down 🔉"
    elif fingers == [0, 1, 1, 0, 0]:
        return "Next ▶▶"
    elif fingers == [1, 0, 0, 0, 1]:
        return "Mute 🔇"
    else:
        return "Unknown
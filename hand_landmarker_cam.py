import cv2
from mediapipe import solutions

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_with_keypoints.avi', fourcc, 20.0, (640, 480))

# Inicializar o modelo do MediaPipe
mp_hands = solutions.hands
mp_drawing = solutions.drawing_utils
hand_detector = mp_hands.Hands(static_image_mode=False, max_num_hands=2)

if not cap.isOpened():
    print("Erro ao acessar a webcam")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand_detector.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:mp_drawing.draw_landmarks(
                frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Webcam com Keypoints', frame)
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()

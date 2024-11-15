import cv2
from mediapipe import solutions

image_path = 'hand.jpg'
image = cv2.imread(image_path)

# Inicializar o modelo do MediaPipe
mp_hands = solutions.hands
mp_drawing = solutions.drawing_utils
hand_detector = mp_hands.Hands(static_image_mode=True, max_num_hands=2)

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
result = hand_detector.process(rgb_image)

if result.multi_hand_landmarks:
    for hand_landmarks in result.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,hand_landmarks,mp_hands.HAND_CONNECTIONS)

output_image_path = 'output_hand_keypoints.jpg'

cv2.imwrite(output_image_path, image)
cv2.imshow('Imagem com keypoints', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import imageio

# config
video_path = "output_euamovoce_keypoints.avi"
output_gif = "teste.gif"
text = "eu amo voce"
frame_rate = 10

cap = cv2.VideoCapture(video_path)
frames = list()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frames.append(frame_rgb)

cap.release()

imageio.mimsave(output_gif, frames, fps=frame_rate)
print(f"GIF salvo como {output_gif}")

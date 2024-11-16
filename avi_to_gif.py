import cv2
from PIL import Image, ImageDraw
import imageio

# config
video_path = "output_euamovoce_keypoints.avi"
output_gif = "output_euamovoce_keypoints.gif"
text = "eu amo voce"
frame_rate = 10

cap = cv2.VideoCapture(video_path)
frames = list()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(frame_rgb)
    draw = ImageDraw.Draw(pil_img)

    text_bbox = draw.textbbox((0, 0), text, font=None)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    draw.rectangle([(0, pil_img.height - text_height - 25), (pil_img.width, pil_img.height)],fill="black")
    draw.text(((pil_img.width - text_width) / 2, pil_img.height - text_height - 20),text,fill="white",font=None,font_size=20)

    frames.append(pil_img)

cap.release()

imageio.mimsave(output_gif, frames, fps=frame_rate)
print(f"GIF salvo como {output_gif}")

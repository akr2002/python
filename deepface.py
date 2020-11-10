from deepface import DeepFace
from PIL import Image
import cv2
import matplotlib.pyplot as plt

img_path = 'img7.jpg'
img = cv2.imread(img_path)
plt.imshow(img[:, :, ::-1])

image = Image.open(img_path)
image.show()

print(img)

print("Age: ", demography["age"])
print("Gender: ", demography["gender"])
print("Emotion: ", demography["dominant_emotion"])
print("Race: ", demography["dominant_race"])

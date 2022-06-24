import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt

imgpath = # IMAGE URL GOES HERE
image = cv2.imread(imgpath)

plt.imshow(image[:, :, ::-1])
plt.show()

analyze = DeepFace.analyze(img_path=imgpath, enforce_detection=False)
emotion = analyze['dominant_emotion']
age = analyze['age']
gender = analyze['gender']
race = analyze['dominant_race']
print(f'{emotion} {age} year old {race} {gender}')

import glob, io, os
import dlib
from PIL import Image
import numpy as np

# refs. http://dlib.net/face_recognition.py.html
# .dat from https://github.com/davisking/dlib-models
predictor_path = "/scripts/dlib/shape_predictor_5_face_landmarks.dat"
face_rec_model_path = "/scripts/dlib/dlib_face_recognition_resnet_model_v1.dat"

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)

def recognition(file):
    img = np.array(Image.open(file).convert('RGB'))

    dets = detector(img, 1)
    print(file, len(dets))

print(glob.glob('/test_images/*'))
for file in glob.glob('/test_images/*'):
    recognition(file)
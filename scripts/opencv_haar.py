import glob, os
import cv2

# refs. https://qiita.com/hitomatagi/items/04b1b26c1bc2e8081427
HaarDir = '/usr/local/share/OpenCV/haarcascades'
face_cascade = cv2.CascadeClassifier(os.path.join(HaarDir, "haarcascade_frontalface_default.xml"))

def recognition(file):
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    print(file, faces)

print(glob.glob('/test_images/*'))
for file in glob.glob('/test_images/*'):
    recognition(file)
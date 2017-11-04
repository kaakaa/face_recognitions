import glob
import face_recognition

def recognition(file):
    image = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(image)
    print(file, face_locations)

print(glob.glob('/test_images/*'))
for file in glob.glob('/test_images/*'):
    recognition(file)
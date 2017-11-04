#!/bin/sh
docker run \
  -v $PWD/test_images:/test_images \
  -v $PWD/scripts:/scripts \
  scooterdelta/face_recognition /scripts/ageitgey_face_recognition.py

docker run \
  -v $PWD/test_images:/test_images \
  -v $PWD/scripts:/scripts \
  --entrypoint python \
  jjanzic/docker-python3-opencv /scripts/opencv_haar.py

docker build -t dlib_skimage_python -f Dockerfile_dlib .
docker run \
  -v $PWD/test_images:/test_images \
  -v $PWD/scripts:/scripts \
  --entrypoint python \
  dlib_skimage_python /scripts/dlib_python.py


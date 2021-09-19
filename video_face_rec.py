import face_recognition
import os
import cv2

video = cv2.VideoCapture(0)

KNOWN_FACES_DIR = "known_faces"
TOLERANCE = 0.4
FRAME_THICKNESS = 1
FONT_THICKNESS = 2
MODEL = "hog" # hog

print("Loading Known Faces")

known_faces = []
known_names = []

for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
        encoding = face_recognition.face_encodings(image) [0]
        known_faces.append(encoding)
        known_names.append(name)

while True:
    ret, image = video.read()
    locations = face_recognition.face_locations(image, model=MODEL)
    encodings = face_recognition.face_encodings(image, locations)

    for face_encoding, face_location in zip(encodings, locations):
        top, right, bottom, left = face_location
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None

        if True in results:
            match = known_names[results.index(True)]
            # print(f"match found: {match}")

            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])

            color = [255, 255, 255]

            cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2]+22)

            cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
            cv2.putText(
                image,
                match,
                (face_location[3]+10, face_location[2]+15),
                cv2.QT_FONT_NORMAL,
                0.5,
                (0, 0, 0),
                FONT_THICKNESS)
    
    cv2.imshow(filename, image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
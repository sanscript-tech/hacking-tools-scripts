# Importing the OpenCV Library
import cv2

# Creating the Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Capture Video from WebCam
video_capture = cv2.VideoCapture(0)

def detect(gray, frame):
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	# Draws a rectangle around the detected faces
	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)
		
	return frame

while True:
	# If frame is read correctly, the return value of `video_capture.read()` is true
	_, frame = video_capture.read()
	# Converting frame to grayscale because OpenCV is more accurate with gray scale videos/images
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	canvas = detect(gray, frame)
	# Displays Webcam with the specified video title
	cv2.imshow("Face-Detection", canvas)

	# Quit the program using `q` key from keyboard
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()
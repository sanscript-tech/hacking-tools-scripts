# Importing the OpenCV Library
import cv2

# Creating the Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# To detect face in image or video
def detect(gray, frame):
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	# Draws a rectangle around the detected faces
	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)
	return frame

# Face Detection in an Image
def imageDetection():
	# Get the Image Location
	filepath = input("Enter the full path to the image: ")
	# Reading Image
	img = cv2.imread(filepath)
	# Converting Image to GrayScale for better accuracy
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img = detect(gray, img)
	# Finally displaying the resultant image
	cv2.imshow("Face Detection", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# Face Detection in live video
def liveDetection():
	# Capture Video from WebCam
	video_capture = cv2.VideoCapture(0)
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

# Menu for the given program
while True:   
	print()
	print("-" * 22, "MENU", "-" * 22)
	print("Press 1 for Face Detection in an Image")
	print("Press 2 to Live Face Detection from Webcam")
	print("Press 3 to Quit")
	print("-" * 50)

	choice = int(input("Enter the menu option: "))

	if choice == 1:
		imageDetection()
	elif choice == 2:
		liveDetection()
	elif choice == 3:
		break
	else:
		print("\nInvalid Choice. Enter a valid option!")
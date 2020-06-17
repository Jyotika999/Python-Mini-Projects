import cv2, glob


all_images = glob.glob("*.jpg")   ##this will read all the images that are present in the same folder with extension .jpg

detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
##we are using harcascade classifier because we want to detect the faces
##if you want to detect some other objects like car or smile or eyes , then the identity you want to search for that particular entity's haarcascade file

##since,here we are going to detect faces from a group of images , so what we have to do is iterate over a loop , picking up the first image and then checking for face detection , similary we will pick the second one and then iterate over


for image in all_images:
	img = cv2.imread(image)  ##to basically read the image
	gray =   cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                ##converting the read image to a grayscale image
	faces = detect.detectMultiScale(gray, 1.1 , 5)

	for (x, y , w ,h ) in faces:
		final_img = cv2.rectangle(img, (x,y) , (x+w,y+h) ,(0 , 255 , 0) , 2)


	cv2.imshow("FACE DETECTION" , final_img)
	cv2.waitKey(2000)
	cv2.destroyAllWindows()

##show the image and have a wait key and then destroy my window



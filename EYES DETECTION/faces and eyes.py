import cv2

detect_face= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
detect_eye = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

imp_img = cv2.VideoCapture("MARK1.jpg")  
 # for using webcam you can give argumnet as 0 or 1 according to the functionality of your webcam else you can directly give the name of the file of the image within the argumnets
 

 ##to read an image that will either return true or false whether the given function have read the image then, it will return true else it will return false
res, img = imp_img.read()  ##second thing is we will get the dimensions of the image that is basically the pixel dimansion
      ## for the above given read dunction that will read the image the avariable res will return true of false that whether the image was detected or not and the variable img will detect the dimensions of the image that will be the pixel dimensions basically


##now here comes the need to convert the read image into the grayscale image because of the constraint of haarcascade.xml module for face detection

##for converting our image innto grayscale , we just need to use a CVT color 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #cvt color function basically converting RGB COLORS TO GRAY SCALE


##for the image read by us , we need to detect the faces of different sizes in our input image

faces = detect_face.detectMultiScale(gray, 1.5, 6)

##we will get the coordinates in the form of x,y , width and height . since we know from one coordinate and width, height known we can easily draw a square over the face or so similarly

for(x , y , w , h) in faces:
	cv2.rectangle(img, (x,y) , (x+w,y+h) ,(255,255,0) , 2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h , x:x+w]


	#for detecting the eyes of diffrent sizes in the image input
	eyes = detect_eye.detectMultiScale(roi_gray)

	#to draw rectangles around eyes
	for (ex, ey, ew, eh) in eyes:
		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


cv2.imshow("ELON IMAGE ", img)   # the inbuilt function imshow will be having two arguments with the first one showing the title of the window opened and the second one will be with respect to 


##now after showing our image we will have three steps every time , which will be wait key , release of image and then destroy of image 
cv2.waitKey(0) ## time for which i need to open the window of the image , preferbly 0 so that you can close whenever you want 

#to close the window
imp_img.release()

# to de allocate any associated memory usage
cv2.destroyAllWindows()
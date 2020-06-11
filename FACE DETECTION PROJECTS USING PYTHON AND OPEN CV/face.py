import cv2

cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imp_img = cv2.VideoCapture("elon.jpg")   # for using webcam you can give argumnet as 0 or 1 according to the functionality of your webcam else you can directly give the name of the file of the image within the argumnets
 

 ##to read an image that will either return true or false whether the given function have read the image then, it will return true else it will return false
 res, img = imp_img.read()  ##second thing is we will get the dimensions of the image that is basically the pixel dimansion
## for the above given read dunction that will read the image the avariable res will return true of false that whether the image was detected or not and the variable img will detect the dimensions of the image that will be the pixel dimensions basically


##now here comes the need to convert the read image into the grayscale image because of the constraint of haarcascade.xml module for face detection

##for converting our image innto grayscale , we just need to use a CVT color 
gray = cv2.cvtColor(img, cv2.COLOR_BRG2GRAY)  #cvt color function basically converting RGB COLORS TO GRAY SCALE


##for the image read by us , we need to detect the faces of different sizes in our input image

faces = detect.detectMultiScale(gray, 1.3, 5)

##we will get the coordinates in the form of x,y , width and height . since we know from one coordinate and width, height known we can easily draw a square over the face or so similarly


cv2.imshow("ELON IMAGE ", img)   # the inbuilt function imshow will be having two arguments with the first one showing the title of the window opened and the second one will be with respect to 


##now after showing our image we will have three steps every time , which will be wait key , release of image and then destroy of image 

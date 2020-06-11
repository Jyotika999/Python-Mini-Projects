FACE DETECTION USING OPENCV :

This Project was done Using fantastic OpenCV Library i.e. "Open Source Computer Vision Library".

The most basic task on Face Recognition is "FACE DETECTION". Before anything , one must first capture a face in order to recognize it or you can even mention of an image which the program can read.

Since, the project is regarding "FACE DETECTION" , therefore an amazing feature of "HaarCascade Classifier" makes that possible to happen.
OpenCV comes witha trainer as well as a detector . If you want to train your own classifier for anything like cars, smile, eyes, etc , you can use OpenCV to create one .




CONCEPTS INVOLVED:

* HAARCASCADE CLASSIFIER IS BEING USED TO DETECT FACES USING OPENCV
* THE IMAGE WILL GET READ USING " .read()  " which will either return true or returns false detecting if it has actually read the image or not . If yes, it will also read the dimensions of the image which will get stored in the assigning variables .
* Now, the image is read , here comes the need of converting the image to a grayscale image because of the constraint of the haarcascade classifier
* Also, for the image read , we need to detect the faces of different sizes and for that " .detectMutiScale() " function takes care of which takes arguments as grayscale converted image and other two dimensions.
* We will get the coordinates in the form of x,y , width , height where x and y are the coordinates of the bottom left position . 
Using a for loop we can easily create a rectangle using the above mentioned four parameters using " .rectangle() "  function having four parameters namely , the image to be read , topmost rightcoordinate, color and finally the width of the rectangle to be built .
* Now for the window to show the output we use ".imshow() "  with two parameters one being the title of the pop up window that will show the result and second the name of the image variable where it was read .
* After showing our image , we will have three steps i.e. a waitKey() which will decide for how much time we want the window to remain open , then the release of the image and last one will be to destroy all windows .

Hurray!! we are done with our FACE DETECTION PROJECT!!
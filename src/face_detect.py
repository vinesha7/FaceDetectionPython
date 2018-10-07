import sys
sys.path.append(r"C:\Users\USER\Anaconda3\Lib\site-packages")

import cv2

#the program takes 1 parameter
#if len(sys.argv) != 2:
#    sys.exit("argument error")
    
#Reading input for image path
imagePath = "test.jpg";

cascPath = "haarcascade_frontalface_default.xml"

#Apply the classifier
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Now we find the faces in the image. If faces are found, it returns the positions of detected faces as Rect(x,y,w,h).
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

s_img = cv2.imread("small_test.jpg")

x_offset=y_offset=50


# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    image[y:y+s_img.shape[0], x:x+s_img.shape[1]] = s_img
    

    
cv2.imshow("Faces found", image)

cv2.waitKey(0)

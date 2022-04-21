import cv2

# img = cv2.imread("./dataset/images/maksssksksss48.png") //this can used when we need to read the image from localstorage

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _,img = cap.read()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray , 1.1 , 4)
    
    for(x , y , w , h) in faces:
        cv2.rectangle(img , (x,y) , (x+y , w+h) , (255 , 0 , 0) , 3)
        
    cv2.resize(img, (1050, 1610))
    cv2.imshow("img" , img)
    
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
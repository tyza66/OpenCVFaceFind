import cv2

img = cv2.imread(r"lenna.png")
gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gary, scaleFactor=1.05, minNeighbors=5)
for x,y,w,h in faces:
    img2 = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("Lenna_find",img2)
k = cv2.waitKey(0)
if k == 115:
    cv2.imwrite(r'Lenna_grey_silm_good_good.png', img)
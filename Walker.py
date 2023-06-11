import cv2

body_classifier=cv2.CascadeClassifier('haarcascade_fullbody.xml')

frame = 1
while frame < 6:
  print(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
  frame += 1 

  bodies=body_classifier.detectMultiScale(gray, 1.2,3)

  for (x,y,w,h) in bodies:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("img",frame)
cv2.waitKey(0)


import cv2
cap=cv2.VideoCapture(0)

while(cap.isOpened()):
  ret,bg=cap.read()
  if(ret):
    bg = cv2.flip(bg, 1)   # 1 = horizontal flip , Flip the frame horizontally to remove the mirror effect
    cv2.imshow("image",bg)
    if cv2.waitKey(30) == ord('q'):
      cv2.imwrite("image.jpg",bg)
      break
cap.release()
cv2.destroyAllWindows()



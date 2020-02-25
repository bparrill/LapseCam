import cv2 as cv

cam = cv.VideoCapture(0, cv.CAP_DSHOW)
#cam.set(cv.CAP_PROP_FRAME_WIDTH, 1280.0)
#cam.set(cv.CAP_PROP_FRAME_HEIGHT, 720.0)
return_value, image = cam.read()
cv.imwrite('testout.png', image)

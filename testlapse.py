import time

import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280.0)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720.0)

cv2.namedWindow("test")
cv2.resizeWindow('test', 1280, 720)

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    img_name = f'pic-{img_counter:06d}.png'
    print(f'Writing {img_name}')
    cv2.imwrite(img_name, frame)
    img_counter += 1
    #time.sleep(5)

    k = cv2.waitKey(5000)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

cam.release()

cv2.destroyAllWindows()
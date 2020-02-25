import cv2

start = 0
end = 27108

index = start

# Get the size, assuming all images are the same
frame = cv2.imread(f'pic-{index:06d}.png')
height, width, layers = frame.shape

vid = cv2.VideoWriter('lapse.avi', 0, 20, (width, height))

for img_counter in range(start, end+1):
    img_name = f'pic-{img_counter:06d}.png'
    vid.write(cv2.imread(img_name))

cv2.destroyAllWindows()
vid.release()

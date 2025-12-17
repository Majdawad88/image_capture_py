# git clone https://github.com/Majdawad88/image_capture_py.git
from picamera2 import Picamera2

import cv2, time

 

print("Initializing Pi Camera…")

picam2 = Picamera2()

 

# Configure a simple preview stream (1280x720 RGB)

picam2.preview_configuration.main.size = (1280, 720)

picam2.preview_configuration.main.format = "RGB888"

picam2.configure("preview")

 

print("Starting camera…")

picam2.start()

time.sleep(0.3) # short warm-up

 

# Capture a single frame (RGB)

frame = picam2.capture_array()

 

# Show the frame

cv2.imshow("Frame (PiCamera2)", frame)

key = cv2.waitKey(0) # 0 = wait indefinitely for a key

 

# Save the image

cv2.imwrite("saved_img.jpg", frame)

print("Saved to saved_img.jpg")

 

# Cleanup

print("Stopping camera.")

picam2.stop()

cv2.destroyAllWindows()

print("Done.")

# git clone https://github.com/Majdawad88/image_capture_py.git
from picamera2 import Picamera2
import cv2, time

print("Initializing Pi Camera...")
picam2 = Picamera2()

# Configure stream
picam2.preview_configuration.main.size = (1280, 720)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")

print("Starting camera...")
picam2.start()
time.sleep(0.3)

# Capture a single frame
frame = picam2.capture_array()

# --- COMMENT OUT OR REMOVE THESE GUI LINES ---
# cv2.imshow("Frame (PiCamera2)", frame)
# key = cv2.waitKey(0)
# ----------------------------------------------

# Save the image (This works without a display)
cv2.imwrite("saved_img.jpg", frame)
print("Saved to saved_img.jpg")

# Cleanup
print("Stopping camera.")
picam2.stop()
# cv2.destroyAllWindows() # Also comment this out
print("Done.")

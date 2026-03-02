# git clone https://github.com/Majdawad88/image_capture_py.git
import cv2
import time
from picamera2 import Picamera2

print("Initializing Pi Camera...")
picam2 = Picamera2()

# Full sensor resolution (prevents zoom)
config = picam2.create_video_configuration(main={"size": (1296, 972)})
picam2.configure(config)

print("Starting camera...")
picam2.start()

# --- Window Setup ---
window_name = "Photo Timer"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL) 
# Resize the display window to something manageable (e.g., 800x600)
cv2.resizeWindow(window_name, 800, 600)
# Move to middle of screen (Adjust 500, 200 based on your monitor resolution)
cv2.moveWindow(window_name, 500, 200)

start_time = time.time()
countdown_duration = 15

print(f"Starting {countdown_duration} second countdown...")

try:
    while True:
        frame = picam2.capture_array()
        
        elapsed = time.time() - start_time
        remaining = countdown_duration - int(elapsed)
        
        if remaining > 0:
            font = cv2.FONT_HERSHEY_SIMPLEX
            text = str(remaining)
            
            # Draw text
            cv2.putText(frame, text, (554, 504), font, 10, (0, 0, 0), 20, cv2.LINE_AA)
            cv2.putText(frame, text, (550, 500), font, 10, (255, 255, 0), 15, cv2.LINE_AA)
            
            cv2.imshow(window_name, frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("\nTaking photo...")
            picam2.capture_file("majd.jpg")
            print("Saved to majd.jpg")
            break

finally:
    picam2.stop()
    cv2.destroyAllWindows()

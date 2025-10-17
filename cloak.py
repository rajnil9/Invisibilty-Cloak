import cv2
import numpy as np
import time

print("Starting Invisible Cloak... Press 'q' to quit")

# Initialize webcam with faster settings
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # DirectShow for quicker startup on Windows
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

# Quick warm-up 
print("Warming up camera...")
for _ in range(10):
    ret, _ = cap.read()
    if ret:
        break
time.sleep(0.5)  # short stabilization

# Capture background quickly
print("Capturing background... Please stay out of frame.")
background_frames = []
for i in range(15):  # reduced frame count for faster start
    ret, bg = cap.read()
    if ret:
        background_frames.append(bg)
if background_frames:
    background = np.median(background_frames, axis=0).astype(np.uint8)
    background = np.flip(background, axis=1)
else:
    print("Warning: Could not capture background properly.")
    ret, background = cap.read()
    background = np.flip(background, axis=1)

print("Background captured. Cloak mode ON.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Color range
    lower_cloth = np.array([80, 60, 60])
    upper_cloth = np.array([110, 255, 255])
    mask = cv2.inRange(hsv, lower_cloth, upper_cloth)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=1)

    mask_inv = cv2.bitwise_not(mask)
    cloak_area = cv2.bitwise_and(background, background, mask=mask)
    rest_area = cv2.bitwise_and(frame, frame, mask=mask_inv)
    final_output = cv2.addWeighted(cloak_area, 1, rest_area, 1, 0)

    cv2.imshow("Invisible Cloak", final_output)

    key = cv2.waitKey(1)
    if key != -1 and chr(key & 0xFF).lower() == 'q':
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()

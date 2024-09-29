import cv2
import numpy as np

def replace_background(frame, background, lower_bound, upper_bound):
    background_resized = cv2.resize(background, (frame.shape[1], frame.shape[0]))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    mask_inv = cv2.bitwise_not(mask)
    
    foreground = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    background_part = cv2.bitwise_and(background_resized, background_resized, mask=mask)
    
    result = cv2.add(foreground, background_part)
    
    return result

lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

cap = cv2.VideoCapture(r'c:\Users\Harshit\Downloads\2024-09-29 11-53-22 - Trim.mp4')

background = cv2.imread(r'c:\Users\Harshit\Downloads\YeYIYbf.jpg')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video_with_background.mp4', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    result = replace_background(frame, background, lower_green, upper_green)
    
    cv2.imshow('Result', result)
    
    out.write(result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

import cv2
import numpy as np

# Function to remove the background color (green screen or any color you want) and replace it with a new background
def replace_background(frame, background, lower_bound, upper_bound):
    # Resize the background to the same size as the frame
    background_resized = cv2.resize(background, (frame.shape[1], frame.shape[0]))

    # Convert the frame to HSV (Hue, Saturation, Value) color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a mask for the specified color range (green in this case)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    # Invert the mask so that we keep everything that is NOT green
    mask_inv = cv2.bitwise_not(mask)
    
    # Extract the non-green part of the frame (the foreground subject)
    foreground = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    # Extract the green part of the frame (the background) and replace it with the new background
    background_part = cv2.bitwise_and(background_resized, background_resized, mask=mask)
    
    # Combine the foreground (non-green) with the new background
    result = cv2.add(foreground, background_part)
    
    return result

# Define the lower and upper bounds for green color in HSV space
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

# Open the video file or webcam (set '0' to use webcam or video file path)
cap = cv2.VideoCapture(r'c:\Users\Harshit\Downloads\2024-09-29 11-53-22 - Trim.mp4')

# Load the background image
background = cv2.imread(r'c:\Users\Harshit\Downloads\YeYIYbf.jpg')

# Video writer to save the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for output file
out = cv2.VideoWriter('output_video_with_background.mp4', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Replace the green screen with the custom background
    result = replace_background(frame, background, lower_green, upper_green)
    
    # Show the result in real-time
    cv2.imshow('Result', result)
    
    # Write the frame to the output video
    out.write(result)
    
    # Press 'q' to exit the video early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects
cap.release()
out.release()

# Close all windows
cv2.destroyAllWindows()

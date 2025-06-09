# 🎥 Background Replacement using OpenCV

This project demonstrates how to **replace a green screen background in a video** with a custom image using OpenCV and Python. It's a practical computer vision project that showcases the power of **color masking and blending** techniques in real-time video processing.

## 📌 Features

- Detects and removes green background using HSV color space.
- Replaces green screen with a custom image.
- Processes each frame of a video and saves the output.
- Real-time visualization of the replacement.

## 🧠 Tech Stack

- Python
- OpenCV
- NumPy

## 📁 File Structure

📂 green-screen-replacer/
├── main.py # Python script with complete background replacement logic
├── output_video_with_background.mp4 # Final rendered video
├── input_video.mp4 # Input video file (green screen)
├── background.jpg # Background image to overlay
└── README.md # Project documentation

## ▶️ How It Works

1. Read the input video using `cv2.VideoCapture`.
2. Convert each frame from BGR to HSV color space.
3. Create a mask using the defined green HSV range.
4. Invert the mask to extract the non-green parts (foreground).
5. Replace green areas with the resized custom background.
6. Merge the foreground and new background using `cv2.add`.
7. Save the processed video and optionally display it in a window.

## 🧪 Example Code Snippet

```python
def replace_background(frame, background, lower_bound, upper_bound):
    background_resized = cv2.resize(background, (frame.shape[1], frame.shape[0]))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    mask_inv = cv2.bitwise_not(mask)
    foreground = cv2.bitwise_and(frame, frame, mask=mask_inv)
    background_part = cv2.bitwise_and(background_resized, background_resized, mask=mask)
    result = cv2.add(foreground, background_part)
    return result

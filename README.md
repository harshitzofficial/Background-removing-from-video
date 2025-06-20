---
# 🎥 Background Replacement using OpenCV

This project demonstrates how to replace a green screen background in a video with a custom image using **OpenCV** and **Python**. It's a practical computer vision project that showcases the power of color masking and blending techniques in real-time video processing.

---

## 📌 Features

- ✅ Detects and removes green background using HSV color space
- ✅ Replaces green screen with any custom image
- ✅ Processes each frame of a video and saves the output
- ✅ Real-time preview using Streamlit
- ✅ Downloadable final video output
---

## 🧠 Tech Stack

- **Python 3.x**
- **OpenCV**
- **NumPy**
- **Streamlit** (for UI)

---

## ▶️ How It Works

1. Reads the input video using `cv2.VideoCapture`
2. Converts each frame from BGR to HSV color space
3. Creates a mask based on a defined green HSV range
4. Inverts the mask to extract non-green (foreground) parts
5. Replaces green areas with the resized custom background
6. Merges the two using `cv2.add`
7. Displays the processed result and allows it to be downloaded

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
````

## 🖼️ Sample Output

### 🎬 Original Video:
[🔗 Watch Original Video](https://github.com/user-attachments/assets/ddd5643c-4826-4ff3-abba-6ee35443a562)

---

### 🌄 Background Image Used:
![Background Image](https://github.com/user-attachments/assets/42beeeb8-5745-4042-9b8e-a629ad6a8d5f)

---

### 🎥 Output Video (with Background Replaced):
[🔗 Watch Output Video](https://github.com/user-attachments/assets/63d02824-0673-4a84-b9ce-5c2a9853674c)


---

## ⚙️ Setup Instructions

### 📁 1. Clone the Repository

```bash
git clone https://github.com/harshitzofficial/Background-removing-from-video.git
cd Background-removing-from-video
```

---

### 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### ▶️ 3. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 🎯 HSV Range Used for Green

```python
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])
```

You can tweak the HSV values if your green screen has a different shade.

---

Made with ❤️ by [Harshit Singh](https://github.com/harshitzofficial)

```

import streamlit as st
import cv2
import numpy as np
import tempfile
import os

# --- Background Replacement Function ---
def replace_background(frame, background, lower_bound, upper_bound):
    background_resized = cv2.resize(background, (frame.shape[1], frame.shape[0]))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    mask_inv = cv2.bitwise_not(mask)
    foreground = cv2.bitwise_and(frame, frame, mask=mask_inv)
    background_part = cv2.bitwise_and(background_resized, background_resized, mask=mask)
    result = cv2.add(foreground, background_part)
    return result

# --- Streamlit UI ---
st.title("🎥 Green Screen Background Replacer")

st.markdown("Upload a video with a green screen and a background image to replace it.")

video_file = st.file_uploader("Upload Green Screen Video", type=["mp4", "avi", "mov"])
bg_image_file = st.file_uploader("Upload Background Image", type=["jpg", "jpeg", "png"])

# HSV range for green
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

if video_file and bg_image_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_img:
        temp_img.write(bg_image_file.read())
        bg_path = temp_img.name

    st.success("Files uploaded successfully!")

    if st.button("🎬 Process Video"):
        st.info("Processing... Please wait.")

        cap = cv2.VideoCapture(video_path)
        background = cv2.imread(bg_path)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        output_path = os.path.join(tempfile.gettempdir(), "output_video.mp4")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        progress = st.progress(0)

        for i in range(frame_count):
            ret, frame = cap.read()
            if not ret:
                break
            result = replace_background(frame, background, lower_green, upper_green)
            out.write(result)
            progress.progress((i + 1) / frame_count)

        cap.release()
        out.release()

        st.video(output_path)
        with open(output_path, "rb") as f:
            st.download_button("⬇️ Download Result", f, file_name="green_screen_replaced.mp4")


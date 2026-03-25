import streamlit as st
import cv2
import numpy as np

# Ito yung Simple UI
st.title("DevOps x WebEngr: Image Processor")
st.write("Upload an image to apply custom automated filters.")

# File Uploader sa website
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert yung in-upload na file para mabasa ng OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # Interactive Dropdown menu
    filter_type = st.selectbox("Select Filter Technique", ["Original", "Thermal Vision", "Motion Blur", "Mirror Flip"])

    result_img = img.copy()

    # Apply filters based on choice
    if filter_type == "Thermal Vision":
        result_img = cv2.applyColorMap(img, cv2.COLORMAP_JET)
    elif filter_type == "Motion Blur":
        kernel_size = 15
        kernel = np.zeros((kernel_size, kernel_size))
        kernel[int((kernel_size-1)/2), :] = np.ones(kernel_size) / kernel_size
        result_img = cv2.filter2D(img, -1, kernel)
    elif filter_type == "Mirror Flip":
        result_img = cv2.flip(img, 1)

    # Convert color from BGR (OpenCV format) to RGB (Web format)
    original_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result_rgb = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)

    # I-display sa website side-by-side
    col1, col2 = st.columns(2)
    with col1:
        st.header("Before")
        st.image(original_rgb, use_column_width=True)
    with col2:
        st.header("After")
        st.image(result_rgb, use_column_width=True)
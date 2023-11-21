import cv2
import streamlit as st
import numpy as np
from PIL import Image

st.header("Image to Sketch!")
def main():
    st.title("Image Selector and Viewer")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "gif", "bmp"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("File details:")
        st.write("Name:", uploaded_file.name)
        st.write("Size:", uploaded_file.size, "bytes")

        if st.button("Convert"):
            converted_image = convert_image(image)
            st.download_button(
                label="Download",
                data=converted_image,
                file_name="converted_image.png",
                key="converted_image_button"
            )
            st.image(converted_image, caption="Converted Image", use_column_width=True)        

def convert_image(image):
    img_np = np.array(image)
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGBA2BGR)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (21, 21), 0, 0)
    img_blend = cv2.divide(img_gray, img_blur, scale=1.5)
    img_blend_rgba = cv2.cvtColor(img_blend, cv2.COLOR_GRAY2RGBA)
    return Image.fromarray(img_blend_rgba)



if __name__ == "__main__":
    main()

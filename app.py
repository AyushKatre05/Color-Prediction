import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Color Detector")

# Function to get color name
def colorName(R, G, B):
    min_dist = 10000
    for i in range(len(ds)):
        d = abs(R - int(ds.loc[i, "R"])) + abs(G - int(ds.loc[i, "G"])) + abs(B - int(ds.loc[i, "B"]))
        if d <= min_dist:
            min_dist = d
            cname = ds.loc[i, 'color_name']
    return cname

# Read colors data
index = ["color", "color_name", "hex", "R", "G", "B"]
ds = pd.read_csv('colors.csv', names=index, header=None)

# Load image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Convert uploaded file to PIL image
    image = Image.open(uploaded_file)

    st.image(image, caption='Uploaded Image')

    # Process image pixel by pixel to get color information
    img_array = np.array(image)
    height, width, _ = img_array.shape

    for y in range(height):
        for x in range(width):
            R, G, B = img_array[y, x]
            color = colorName(R, G, B)
            st.text(f"Pixel at ({x}, {y}): {color} (R={R}, G={G}, B={B})")

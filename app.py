import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw

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
    img_draw = ImageDraw.Draw(image)

    st.image(image, caption='Uploaded Image')

    # Process image when double-clicked
    if st._is_running_with_streamlit:
        st.write("Double-click on the image to detect color")

    clicked = False

    # Mouse event callback function
    def draw_fun(x, y):
        global clicked
        global img_draw
        global image
        
        clicked = True
        b, g, r = image.getpixel((x, y))
        b = int(b)
        g = int(g)
        r = int(r)

        img_draw.rectangle([10, 10, 250, 60], fill=(b, g, r))
        text = colorName(r, g, b) + ' R =' + str(r) + ' G= ' + str(g) + ' B= ' + str(b)
        img_draw.text((50, 50), text, fill=(255, 255, 255))
        if r + g + b >= 600:
            img_draw.text((50, 50), text, fill=(0, 0, 0))

    while True:
        # Click event handling
        click_pos = st.experimental_get_query_params().get("position")
        if click_pos:
            x, y = map(int, click_pos[0].split(","))
            draw_fun(x, y)
            st.image(image, caption='Detected Color')

import streamlit as st
import numpy as np
import pandas as pd
import cv2

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
    # Convert uploaded file to OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    st.image(img, channels="BGR", caption='Uploaded Image')

    clicked = False

    # Mouse event callback function
    def draw_fun(event, x, y, flags, param):
        global b, g, r, xpos, ypos, clicked
        if event == cv2.EVENT_LBUTTONDBLCLK:
            clicked = True
            xpos = x
            ypos = y
            b, g, r = img[y, x]
            b = int(b)
            g = int(g)
            r = int(r)

    cv2.namedWindow('Color Detect')
    cv2.setMouseCallback('Color Detect', draw_fun)

    while True:
        cv2.imshow('Color Detect', img)
        if clicked:
            cv2.rectangle(img, (10, 10), (250, 60), (b, g, r), -1)
            text = colorName(r, g, b) + ' R =' + str(r) + ' G= ' + str(g) + ' B= ' + str(b)
            cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            if r + g + b >= 600:
                cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
            clicked = False
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

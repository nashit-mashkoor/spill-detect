import streamlit as st
import requests
import json
import warnings

from PIL import Image, ImageDraw, ImageFont


# Ignore all warnings
warnings.filterwarnings("ignore")

def annotate_image(image, text, bbox=None):
    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define the font properties
    font = ImageFont.load_default()
    font_color = (0, 0, 0)

    # Get the size of the text
    text_size = draw.textsize(text, font)

    # Calculate the position of the text
    x = (image.width - text_size[0]) // 2
    y = (image.height - text_size[1]) // 2

    # Write the text on the image
    draw.text((x, y), text, font=font, fill=font_color)

    if not bbox:
        return image

    # Draw the bounding box
    draw.rectangle((coordinates["xmin"], coordinates["ymin"], coordinates["xmax"], coordinates["ymax"]), outline='red')

    # Return the modified image
    return image

# App setting
st.set_page_config(
    page_title="Spillage Detector", layout="wide", initial_sidebar_state="collapsed",
    page_icon='💽'
)
HIDE_STREAMLIT_STYLE = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(HIDE_STREAMLIT_STYLE, unsafe_allow_html=True)

st.snow()
_, col, _ = st.columns([3, 2, 3])
with col:
    st.title("Spillage Detector")

image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if not image_file:
    st.warning("Image not uploaded")   
    st.stop()


url = 'https://predict.app.landing.ai/inference/v1/predict?endpoint_id=296fe792-9d60-457e-9637-a6031f54fe4b'
headers = {
    'apikey': st.secrets('api_key'),
    'apisecret': st.secrets('api_secret')
}
files = {
    'file': image_file
}
response = requests.post(url, headers=headers, files=files)
response = json.loads(response.content)
image = Image.open(image_file)

st.write(response)
if response['backbonepredictions'] == {}:
    st.warning("No spillage")
    st.image(image)
    st.stop()

for prediction in response['backbonepredictions'].values():
    label_name = prediction['labelName']
    coordinates =  prediction['coordinates']
    image = annotate_image(image, label_name, coordinates)
    st.info(f'Spillage detected: {label_name}')
    st.image(image)

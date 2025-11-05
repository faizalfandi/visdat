import streamlit as st
from PIL import Image


st.title("PRAKTIKUM 1 VISUALISASI DATA")
st.subheader("Bagian 1. : Data Element")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi = 0110222184
2. Faqih Al Fauzan = 0110222152
3. Afnan Ainul Marddhiyyah = 0110222128
""")

st.write("Displaying an Images")
# Displaying Image by specifying path
st.image("ijal.jpg")
# Image Courtesy by unplash
st.write("Image Courtesy: unplash.com")

import streamlit as st
# Image Courtesy
st.write("Diplaying Multiple Images")
# Listing out animal images
animal_images = [
'ijal.jpg',
'ijal.jpg',
'ijal.jpg',
'ijal.jpg',
]
# Displaying Multiple images with width 150
st.image(animal_images, width=150)
# Image Courtesy
st.write("Image Courtesy: Unplash")


original_image = Image.open("ijal.jpg")
# Display Original Image
st.title("Original Image")
st.image(original_image)

# Resizing Image to 600*400
resized_image = original_image.resize((600, 400))
#Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)

import streamlit as st
import base64
# Function to set Image as Background
def add_local_background_image(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Image Courtesy: unplash")
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:files/("jpg");base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
st.write("Background Image")
# Calling Image in function
add_local_background_image('azril.jpg')
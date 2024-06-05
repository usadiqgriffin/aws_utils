import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("Background Remover")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption='Uploaded Image', use_column_width=True)

    with st.spinner('Removing background...'):
        input_image_bytes = io.BytesIO()
        input_image.save(input_image_bytes, format=input_image.format)
        input_image_bytes = input_image_bytes.getvalue()

        output_image_bytes = remove(input_image_bytes)
        output_image = Image.open(io.BytesIO(output_image_bytes))

    st.image(output_image, caption='Image with Background Removed', use_column_width=True)
    st.success('Background removal completed!')


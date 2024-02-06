# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lyrWK5FQz76ft--kTg50Zp1zhgQfTlES
"""

import streamlit as st
import pickle
import tensorflow as tf
import numpy as np
from PIL import Image

# Function to load the model from the pickle file
def load_model_from_pickle(filepath):
    with open(filepath, 'rb') as f:
        model = pickle.load(f)
    return model

# Load the model
model = load_model_from_pickle('/content/VAN NFT.pkl')

# Define the Streamlit app
def main():
    st.title('Style Transfer App')

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Perform style transfer
        if st.button('Apply Style Transfer'):
            # Preprocess the image
            image = np.array(image)
            # Apply style transfer using your model
            # result_image = model.predict(image)
            # Display result
            # st.image(result_image, caption='Styled Image', use_column_width=True)
            st.write("Style transfer functionality is not yet implemented.")

if __name__ == '__main__':
    main()


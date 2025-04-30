import numpy as np
import tensorflow as tf
import streamlit as st
from PIL import Image

# st.set_page_config(
#     page_title='Data Inference App',
#     layout='centered',
#     initial_sidebar_state='expanded'
# )

def run():
    st.title('Testing CNN Model Performance')
    st.subheader('-Classify an image into categories using a CNN model-')

    @st.cache_resource
    def load_model():
        model = tf.keras.models.load_model("model1_checkpoint.keras") 
        return model

    model = load_model()

    uploaded_file = st.file_uploader('## Upload an image for prediction', type=['jpg', 'png'])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image',  use_container_width =True)

    def preprocess_image(image):
        image = image.resize((300, 300))  
        image_array = np.array(image) / 255.0  
        return np.expand_dims(image_array, axis=0)

    if uploaded_file is not None:
        processed_image = preprocess_image(img)

    if uploaded_file is not None:
        prediction = model.predict(processed_image)
        class_name = ['Bike', 'Car']  
        predicted_class = class_name[0] if prediction[0][0] < 0.5 else class_name[1]
        emoji = '🏍️' if predicted_class == 'Bike' else '🚗'
        st.write(f'### Image Prediction: {predicted_class}  {emoji} (Confidence: {prediction[0][0]:.2f})')

if __name__ == '__main__':
    run()

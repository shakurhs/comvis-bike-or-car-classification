import streamlit as st
from PIL import Image

def run():
    st.title('AI-Powered Image Prediction: Bike or Car')
    st.subheader('-An Exploratory Data Analysis page-')

    image3 = Image.open('eda3GC7.png')
    image2 = Image.open('eda2GC7.png')
    image1 = Image.open('eda1GC7.png')

    col1, col2 = st.columns(2)
    with col1:
        st.image(image3,
                 use_container_width=True
                 )

    with col2:
        st.image(image2,
                 use_container_width=True
                 )

    st.image(image1,
             use_container_width=True,
             caption='Count of File Types (top left), Count of Classes(top right), File Size Distribution and Image Dimension (bottom)'
             )
    
    st.markdown("---")

    st.markdown("[Data Source: Kaggle](https://www.kaggle.com/datasets/utkarshsaxenadn/car-vs-bike-classification-dataset)")

    st.write('The dataset contains a total of 4,000 images, divided into two categories: \n- 2000 images of Bike\n- 2000 images of Car')
    
    st.write('The Bike and Car dataset underwent preprocessing and augmentation before being trained ' \
    'using a CNN model implemented with the Sequential API. ' \
    'The architecture included Convolutional Layers for feature extraction, Max-Pooling Layers to reduce spatial dimensions, ' \
    'Dropout Layers to prevent overfitting, Global Max-Pooling for dimensionality reduction, '
    'and Dense Layers with a Sigmoid activation function for binary classification. ' \
    'The model was trained using the Binary Cross-Entropy loss function and optimized with the Adam Optimizer, ' \
    'achieving an Accuracy score of 84%.')
if __name__ == '__main__':
    run()
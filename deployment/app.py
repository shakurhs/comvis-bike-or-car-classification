import streamlit as st
st.set_page_config(
    page_title='Data Inference App: Bike or Car',
    layout='centered',
    initial_sidebar_state='expanded'
)
import eda
import prediction

page = st.sidebar.selectbox('Page', ('Home', 'Prediction'))

if page == 'Home':
    eda.run()
else:
    prediction.run()
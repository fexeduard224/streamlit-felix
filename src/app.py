import streamlit as st
import numpy as np
import pickle 
from pickle import load


model = pickle.load(open('model.pkl', 'rb'))


st.title('House Price Prediction')


bedrooms = st.number_input('Enter number of bedrooms', min_value=0)
bathrooms = st.number_input('Enter number of bathrooms', min_value=0)
floors = st.number_input('Enter number of floors', min_value=0)
yr_built = st.number_input('Enter year built', min_value=0)


if st.button('Predict'):
    arr = np.array([bedrooms, bathrooms, floors, yr_built]).astype(np.float64)
    prediction = model.predict([arr])
    st.success(f'The predicted price is: {int(prediction)}')
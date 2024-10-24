#Importing necessary libraries

import pandas as pd
import numpy as np
import pickle as pkl
import streamlit as st

model = pkl.load(open('Best_Insurance_Model.pkl','rb'))

# Creating header
st.title('Medical Insurance Premium Predictor')

# Inputs
st.sidebar.header('User Inputs')
gender = st.sidebar.selectbox('Choose Gender', ['Female', 'Male'])
smoker = st.sidebar.selectbox('Are you a smoker?', ['No', 'Yes'])
region = st.sidebar.selectbox('Choose region', ['SouthEast', 'SouthWest', 'NorthEast', 'NorthWest'])
children = st.sidebar.slider('Number of children', 0, 10)
age = st.sidebar.slider('Age', 5, 80)
bmi = st.sidebar.slider('BMI', 10.0, 50.0)

if gender == 'Female':
    gender = 0;
else:
    gender = 1

if smoker == 'No':
    smoker = 0;
else:
    smoker = 1;

if region == 'SouthEast':
    region = 1
elif region == 'SouthWest':
    region = 2
elif region == 'NorthEast':
    region = 3
else:
    region = 4

input_data = (age,gender,bmi,children,smoker,region)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1,-1)


if st.button('Predict Insurance Premium'):
    prediction = model.predict(input_data)
    st.success(f'Estimated Insurance Premium: ${round(prediction[0], 2):,}')
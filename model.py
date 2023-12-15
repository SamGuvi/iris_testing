import streamlit as st
import sklearn
import pandas as pd

import pickle
from sklearn.model_selection import train_test_split

sepel_length = st.sidebar.slider('Sepal Length', 0, 10)
sepel_width = st.sidebar.slider('Sepal Width', 0, 10)
petal_length = st.sidebar.slider('Petal Length', 0, 10)
petal_width = st.sidebar.slider('Petal Width', 0, 10)

X = [[sepel_length, sepel_width, petal_length, petal_width]]

model=pickle.load(open('model.pkl', 'rb'))

bt=st.sidebar.button('Predict')
if bt:
    result = model.predict(X)
    st.title(f'Prediction is {result[0]}')
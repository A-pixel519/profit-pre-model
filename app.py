
import pickle
import streamlit as st
import numpy as np
import pandas as pd


with open("model.pkl",  "rb") as f:
  model = pickle.load(f)

# give the streamlit app page a title
st.title("profit predictor for retailers")

# input widget for getting user value for x(feature matrix value)
sales = st.slider("Total_Sales", min_value=0, max_value=100, value=20)

#after selecting price, the user then submits the price value
if st.button("predict"):
  #take the price value , and format the value the right way
  prediction= model.predict([[sales]])[0].round(2)
  st.write("the predicted operational profit is", prediction,"thousand")


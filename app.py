import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.title("Welcome to Streamlit!")

st.write("Hello, Streamlit!")
st.write(12345)
st.write({"Name": "Alice", "Age": 30})


# Markdown
st.write("**Bold Text** and *Italic Text*")

# number input
age = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=1200,
                      value=25)
st.write(f"Your age is {age}")

option = st.selectbox("Choose your favorite color:",
                      ["Red", "Blue", "Green"])
st.write(f"You selected: {option}")

if st.button("Click Me"):
    st.write("Button clicked!")
else:
    st.write("Button Not clicked!")

st.success("Operation completed successfully!")

st.write("----------------------------------------------------------------------------------------------")

st.title("Streamlit Demo App")
st.header("User Input Section")

st.write("Please provide your details below:")

age1 = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)
color = st.selectbox("Choose your favorite color:",
                     ["Red", "Blue", "Green"])

if st.button("Submit"):
    st.success(f"Thank you! Age: {age1}, Favorite Color: {color}")

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
                      max_value=120,
                      value=25)
st.write(f"Your age is {age}")

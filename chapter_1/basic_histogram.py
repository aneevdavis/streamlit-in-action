import streamlit as st
import matplotlib.pyplot as pyplot
import numpy as np

nums = np.random.normal(1, 1, size=5000)
figure, subplot = pyplot.subplots()

bins = st.number_input("Number of bins", min_value=1, max_value=100)
subplot.hist(nums, bins=bins)
st.pyplot(figure)
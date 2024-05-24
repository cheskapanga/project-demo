import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.write("Hello, let's learn how to build a streamlit app together")

df = pd.read_csv('data/cc_rfm.csv)
st.dataframe(df)

rand = np.random.normal(1, 2, size = 20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

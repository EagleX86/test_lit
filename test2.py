import streamlit as st
import time

st.title("Animated Progress Bar")

progress_bar = st.progress(0)

for i in range(101):
    time.sleep(0.05)  # Simulate a task taking time
    progress_bar.progress(i)
    
st.success("Task Completed!")

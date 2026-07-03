import streamlit as st

#Take a user input\
name= st.text_input("enter your name")

st.title("Take the input")

if st.button("submit"):
  st.write(f"print the name: {name}")

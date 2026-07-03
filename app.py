import streamlit as st
st.title("Take the input")
#Take a user input\
name= st.text_input("enter your name")



if st.button("submit"):
  st.write(f"print the name: {name}")

import streamlit as st 
st.title("simple chatbot")
Question=st.text_input("ask input")
if st.button("send"):
  st.write("you asked",Question)
  st.write("get reply sooonnnnnn")
  
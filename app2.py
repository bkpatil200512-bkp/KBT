import streamlit as st 
st.title("Welcome to the basic streamlit app")
age=st.slider("Select your age",1,100)
city=st.selectbox("select your city",["delhi","mumbai","nasik","pune"])
if st.button("show details"):
  st.write("age", age)
  st.write("city", city)
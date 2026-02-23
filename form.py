import streamlit as st 

st.markdown("""
<style>

          .stButton > button{
            background-color:green;
            color:white;
            border-radius:50%;
          }

""",unsafe_allow_html=True)
import streamlit as st 
st.title("Welcome to the basic streamlit app")
name=st.text_input("enter your name:")
age=st.slider("Select your age",1,100)
city=st.selectbox("select your city",["delhi","mumbai","nasik","pune"])
std=st.selectbox("select your class",[1,2,3,4,5,6,7,8,9,10])
if st.button("show details"):
  st.write("name ", name)
  st.write("age ", age)
  st.write("city ", city)
  st.write("class ", std)
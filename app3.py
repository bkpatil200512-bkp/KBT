import streamlit as st 
st.title("Basic calculator: ")
num1=st.text_input("enetr your first number:")
num2=st.text_input("enetr your second number:")
a=int(num1)
b=int(num2)
operation=st.selectbox("choose op",["add", "sub", "mult","div"])
if st.button("calculate"):
  if operation=="add":
    st.write("addition is",a+b)
  elif operation=="sub":
    st.write("difference is",a-b)
  elif operation=="mult":
    st.write("multiplication is",a*b)
  elif operation=="div":
    if num2!=0:
      st.write("division is",a/b)
    else:
      st.write("not divisible")
  
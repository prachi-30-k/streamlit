import streamlit as st
st.title("Interactive User Interface Example")

#Take text input
user_text = st.text_input("Enter some text:")

#Add a slider
slider_value = st.slider("Select a value:", 0, 100, 50)

#Button interaction
if st.button("Submit"):
    st.write(f"You entered: {user_text}")
    st.write(f"Slider value is: {slider_value}")
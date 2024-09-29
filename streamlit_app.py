import streamlit as st
import os 
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyDw0Ekl8gAdOLEv9IJG9b0KfDyVmgdNJZ8")

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text,image_data,prompt):
    response = model.generate_content([input_text,image_data[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()  #work with images as bytes array
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data" : bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file was uploaded")

st.set_page_config(page_title = "CalcBot")
st.header("CalcBot")
st.sidebar.header("CalcBot")
st.sidebar.write("Made by Mahit")
st.sidebar.write("powered by gemini")
st.subheader("Made by Mahit")
st.subheader("Cheat on your assignments with CalcBot")
input = st.text_input("what do you want me to do?",key="input")
uploaded_file = st.file_uploader("Choose an image ", type = ["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image", use_column_width=True)

ssubmit = st.button("Lets Go")
input_prompt = """
   You are a calculus expert. You can solve any calculus problem. 
   If it is a definite integral, please solve by putting the limits and returning the final answer.
   You will be given an image which will be uploaded. 
   You need to read the image and solve the question with approriate steps and help the user solve the problem.
    
"""

if ssubmit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's what you need to know!")
    st.write(response)

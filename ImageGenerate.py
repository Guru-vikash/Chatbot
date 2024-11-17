from dotenv import load_dotenv

load_dotenv()       #loading all environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#function to load gemini pro model 
model=genai.GenerativeModel('Gemini-1.5-flash-002')

def get_gemini_response(input,image):
    if input!='':
        response=model.generate_content(input,image)
    else:
        response=model.generate_content(image)
    return response.text

#initialize streamlit app
st.set_page_config(page_title='🤡 Image Demo')
st.header('Gemini Image Generate Application ')



input=st.text_input("Input Prompt",key='input')

Upload_file=st.file_uploader('Choose an image ',type=['jpg','jpeg','png'])
image=''
if Upload_file is not None:
    image=Image.open(Upload_file)
    st.image(image,caption='Uploaded Image',use_column_width=True)
    
submit=st.button('Tell me about the image')

#if submit is done 

if submit:
    response=get_gemini_response(input,image)
    st.subheader('Response')
    st.write(response)


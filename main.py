import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai


#load env variable
load_dotenv()


st.set_page_config(
    page_title='Chat With Gemini-Pro',
    page_icon=':brain:',         #image brain
    layout='centered'
)


# st.set_page_config(page_title="Chatbot ",page_icon="🤖")
# st.set_page_config(page_title="Image Generate ",page_icon="🧬")
# st.set_page_config(page_title="Video Generate",page_icon="🎥")

# options = st.multiselect(
#     "What are your favorite colors",
#     ["Green", "Yellow", "Red", "Blue"],
#     ["Yellow", "Red"],
# )

# st.write("You selected:", options)
# st.selectbox("Select your service:")

Google_API_Key=os.getenv("GOOGLE_API_KEY")

#get gemini-pro model
gen_ai.configure(api_key=Google_API_Key)
model=gen_ai.GenerativeModel('gemini-pro')

# function translate
def translate_role_from_Streamlit(user_role):
    if user_role=='model':
        return 'Assistant'
    else:
        return user_role
    
# if "chat_session" not in st.session_state:
#     st.session_state.chat_session=model.start_chat(history=[])

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    st.write("Chat session initialized.")
else:
    st.write("Chat session already exists.")


st.title('🤖 Gemini-Pro ')

for msg in st.session_state.chat_session.history:
    with st.chat_message(translate_role_from_Streamlit(msg.role)):
        st.markdown(msg.parts[0].text)


user_prompt=st.chat_input("Ask Gemini-Pro ......")
if user_prompt:
    st.chat_message('user').markdown(user_prompt)

    #send user msg to gemini-pro and get response

    gemini_response=st.session_state.chat_session.send_message(user_prompt)

    # display response
    with st.chat_message('assistant'):
        st.markdown(gemini_response.text)


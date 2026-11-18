import streamlit as st
from groq import Groq
st.set_page_config(page_title = "AI Interview Assistant", page_icon = '🫡', layout= 'centered')
st.title("AI Interview Asssitant ")
st.caption(" it is a platform for getting information")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNorFound):
                st.error("API Key is missing . Add it in Advance setting")
                st.stop()
role = st.selectbox("JOB TITLE", ['software engineer','senior software engineer', 'data analyst','prompt engineer', 'Devops engineer', 'other'])
if role == "other":
  st.text_input("Enter your job title ","XXXXXXX")
role = st.selectbox("model", ['openai/gpt-oss-safeguard-20b', 'openai/gpt-oss-120b'])

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
gen_model = st.selectbox("model", ['openai/gpt-oss-20b', 'openai/gpt-oss-120b'])
role = st.selectbox("difficult level", ['bigginer','intermidiate','advance'])
mode = st.radio('Activity', ['generate questions', 'generate code questions', 'evaluate answer','improve answers'])
if mode == 'generate questions':
  count = st.slider(1,10,5)
elif mode == 'generate code questions':
  topic = st.selectbox('Topics', ['SQL','AIML','Python','DSA','c++/c','Java','cyber security','ML'])
  count = st.slider("Number od question",1,10,5)
else:
  question = st.text_area('Enter interview question here ')
  answer = st.text_area('enter your answer ', height = 160)

if st.button("Generate AI Response", type = "primary"):
  if mode in ['Evaluate Answers', 'Imporve Answer'] and (not question.strip() or not answer.strip()):
    st.warning("please enter valid question and answer")
    st.stop()
  topics = "Topics is " + topic + "difficlty is " + level 
  if mode == "generate questions":
    task = "generate" + str(count) + "Frequenrtly asked Interview question 3 theory and 2 conceptual. do not give answers. give hints"
  elif mode == "generate code questions":
    task = "generate" + str(count) + "Frequenrtly askedcodeing question on " + topic + " anything can be related to topic "
  elif mode == "evaluate answer":
    task = "question :" + question + "MY Answer : " + answer + "Evalute this answer based on concept, relevence , communication, length of answe. give each rating out of 5 in a list. "
  elif mode == "improve answers":
     task = "question :" + question + "MY Answer : " + answer + "imporve the answern based oon choice on words key words to include. do not invent anything about candidate " 
  background = "job role: " + role + " difficult level: " + level
  with st.spinner(" generating your answer .... "):
    try:
      response = client.chat.completions.create(
        model = gen_model,
        messages = [{"role":"system","content":"Act as a senoir interviewer , both HR and technicall expert"},
                     {"role" : "user",
                     "content" : backgroound + task }],
        temprature = 0.7,
        max_tokens = 2000)
        output = response.choices[0].message.content
        st.subheader("AI Response ")
        st.markdown(output)
        st.download_button("Download response", output , file_name = "Interview_Response.txt", mime = 'text/plain' )
    except Exception as e:
      st.error ("API connection was unsuccessful: ", e)
      st.info ("Please check your API key and rate limits")
st.caption("Powerd by streamlit.io and  github. using LLM API")

#Streamlit is a powerful open-source framework used to create web applications for ML, data science and other related tasks. 
#It simplifies the process of building interactive and customizable web-based user interface (UIs) directly from Python scripts. 

import streamlit as st  #streamlit helps us implements projects  rapidly


#Langchain has built a wrapper around OpenAI APIs which we can get access to all services that OpenAI provides.
from langchain.llms import OpenAI 

#Define a function to return a response of the question asked 
def load_answer(question):
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature = 0)
    answer=llm(question)
    return answer

#App UI starts here 
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

#Define a function to take a text from the user 
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

user_input = get_text()
response=load_answer(user_input)

submit = st.button("Generate")

#If generate button is clicked

if submit:
    st.subheader("Answer:")
    st.write(response)

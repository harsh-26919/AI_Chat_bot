import streamlit as st
import requests

def get_ollama_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
                           json={ 'input':{'topic':input_text}})
    return response.json()['output']['content']
## streamlit framework

st.title('Langchain Demo With smollm2:135m chains ')
input_text=st.text_input("Write a poem on")

if input_text:
    st.write(get_ollama_response(input_text))
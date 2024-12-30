#LANGCHAIN_API_KEY="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"
#LANGCHAIN_PROJECT="FirstProject"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
from langchain_ollama import ChatOllama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


##Langsmith tracking

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

##creating chatbot

prompt=ChatPromptTemplate.from_messages(
    [
       ("system","You are a helpful assistant. Please provide response to the user queries"),
       ("user","Question:{question}")
    ]
)

#streamlit framework

st.title("Langchain Demo with LLama 3.2 API")
input_text=st.text_input("Search the topic you want")

#open AI LLM call
llm =ChatOllama(model="smollm2:135m")
output_parser=StrOutputParser()

## chain
chain=prompt|llm|output_parser 

if input_text:
    st.write(chain.invoke({'question':input_text}))
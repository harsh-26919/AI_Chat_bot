from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A Simple API Server"
)

add_routes(
    app,
    ChatOllama(model="smollm2:135m"),
    path="/ollama"
)

## ollama llm model
llm=ChatOllama(model="smollm2:135m")

prompt=ChatPromptTemplate.from_template("Write me a  poem in hindi language on {topic} for me ")

add_routes(
    app,
    prompt|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
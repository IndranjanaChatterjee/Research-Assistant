from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()

# Check if API key is set
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("Please set your GOOGLE_API_KEY in the .env file")

# Initialize the chat model with simple configuration
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)
chat_history = []

while True:
    user_input=input("Me:")
    chat_history.append(user_input);
    if user_input == 'exit':
        break;
    result=model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI:",result.content)
print(chat_history)
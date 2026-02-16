from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()
# Check if API key is set
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("Please set your GOOGLE_API_KEY in the .env file")

print(os.getenv('GOOGLE_API_KEY'));

# Initialize the chat model with simple configuration
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

message=[
    SystemMessage(content="You are an excellent AI chat Assistant"),
    HumanMessage(content="Tell me about LangChain")
]

result=model.invoke(message)
message.append(AIMessage(content=result.content))
print(message)
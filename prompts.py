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

# Create the prompt and get response
result = model.invoke("Draft a short poem about the sea.")

# Print the response
# print("AI Response:", result.content)

st.header('Research Tool')

user_input=st.text_input('Enter the name of your research paper')

if st.button('Poem'):
    st.write(result.content)
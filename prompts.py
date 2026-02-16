from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
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


# Print the response
# print("AI Response:", result.content)

st.header('Research Tool')


paper_input=st.selectbox("Select Research Paer Name",["Select...","Attention is ALL you need","BERT:Pretraining deep Bidirectional Transformers"])
style_input=st.selectbox("Select Style",["Select...","Beginner-friendly","Code Oriented","Mathematical","Technical"]);
input_length = st.selectbox("Select Style",["Select","Short(1-2 paragraphs)","Medium (3-4 paragraphs)", "Long (Detailed)"])

template=load_prompt('template.json');



if st.button('Summarize'):
    chain = template | model;   #creating chains with template first and model second such that the output of the first is the input of the second which is model
    result=chain.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":input_length,
    })
    
    st.write(result.content)
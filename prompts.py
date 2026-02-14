from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate
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

user_input=st.text_input('Enter the name of your research paper')
paper_input=st.selectbox("Select Research Paer Name",["Select...","Attention is ALL you need","BERT:Pretraining deep Bidirectional Transformers"])
style_input=st.selectbox("Select Style",["Select...","Beginner-friendly","Code Oriented","Mathematical","Technical"]);
input_length = st.selectbox("Select Style",["Select","Short(1-2 paragraphs)","Medium (3-4 paragraphs)", "Long (Detailed)"])

# template
template=PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template="""Please summarize the research paper titled '{paper_input}' with the following specifications:
    Explanation Style: {style_input}
    Explanation Length: {length_input}
    1. Mathematical Details:
     - Include relevant mathematical equations if present in the paper.
     - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
    2. Analogies:
     - Use relatable analogies to simplify complex ideas.
    Ensure the summary is clear, concise, accurate, and aligned with the provided style."""
)

# fill the placeholders
prompt = template.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":input_length,
})

if st.button('Summarize'):
    result = model.invoke(prompt);
    st.write(result.content)
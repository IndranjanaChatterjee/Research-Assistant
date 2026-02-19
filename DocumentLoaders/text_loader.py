from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Check if API key is set
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("Please set your GOOGLE_API_KEY in the .env file")

# Initialize the chat model with simple configuration
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser=StrOutputParser()


text_loader=TextLoader('cricket.txt',encoding='utf-8')
chain= prompt | model | parser


docs=text_loader.load()

result=chain.invoke({'poem': docs[0].page_content})
print(docs)
print(len(docs))
print(docs[0])
print(docs[0].page_content)
print(docs[0].metadata)
print(result)
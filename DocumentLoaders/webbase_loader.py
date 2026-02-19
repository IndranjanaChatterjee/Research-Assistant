from langchain_community.document_loaders import WebBaseLoader
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
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://en.wikipedia.org/wiki/Artificial_intelligence'
loader = WebBaseLoader(url)
docs = loader.load()
chain= prompt | model | parser
result = chain.invoke({'question': 'What is Artificial Intelligence?', 'text': docs[0].page_content})



print(result)
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Check if API key is set
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("Please set your GOOGLE_API_KEY in the .env file")

# Initialize the chat model with simple configuration
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)
parser=JsonOutputParser()

template= PromptTemplate(
    template="Give me the name , age and the city of a frictional person \n {format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain=template | model | parser  #using chains
final_result=chain.invoke({})
print(final_result)
print(final_result['name'])
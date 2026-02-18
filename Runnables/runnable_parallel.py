from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda, RunnableSequence
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

# Check if API key is set
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("Please set your GOOGLE_API_KEY in the .env file")

# Initialize the chat model with simple configuration
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'tweet': prompt1 | model | parser,
    'linkedin_post': prompt2 | model | parser,
}
)

result = parallel_chain.invoke({'topic':'AI'})

print(result['tweet'])
print(result['linkedin_post'])
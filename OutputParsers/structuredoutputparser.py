from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate

# ✅ Try stable parser import
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("Please set your GOOGLE_API_KEY in the .env file")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Write 3 facts about {topic}\n{format_instructions}',
    input_variables=['topic'],  
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)

chain = template | model | parser

final_result = chain.invoke({'topic': 'black hole'})
print(final_result)

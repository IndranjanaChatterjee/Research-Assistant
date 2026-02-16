from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
from typing import TypedDict, Annotated,Optional,Literal
from pydantic import BaseModel,Field
load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("Please set your GOOGLE_API_KEY in the .env file")

print(os.getenv("GOOGLE_API_KEY"))

# Initialize the chat model with simple configuration
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)


# schema
class Review(BaseModel):
    key_themes:list[str]=Field(description="Write down all the key themes discussed in the review in the form of a list")
    summary:str=Field(description="A brief summary of the review")
    sentiment:Literal['pos','neg']=Field(description="Return sentiment of the review , either positive , negative or neutral")
    pros:Optional[list[str]]=Field(default=None,description="Write down all the pros of the review in a list")
    cons:Optional[list[str]]=Field(default=None,description="Write down all the cons of the review in a list")
    name:Optional[str]=Field(default=None,description="Write the name of the reviewer")
    
    
structured_model = model.with_structured_output(Review)

result=structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
The weight and size make it a bit uncomfortable for one-handed use
why do I need five different Samsung apps for things Google already provides
$1,300 price tag is also a hard pill to swallow

Review by Piu Chatterjee
""")

print(result)

# vector_stores.py
import os
import sys
import os
from dotenv import load_dotenv

load_dotenv()  # ← THIS loads .env variables into environment

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document


# --- CONFIG ---
# preferred model name for Gemini embeddings
EMBEDDING_MODEL = "models/gemini-embedding-001"
PERSIST_DIR = "embeddings_db"
COLLECTION_NAME = "sample"

# --- Get API key (checks both environment names) ---
load_dotenv()

# Check if API key is set
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("Please set your GOOGLE_API_KEY in the .env file")

# --- Initialize Gemini embeddings ---
embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL,
    api_key=os.getenv("GOOGLE_API_KEY")  # explicitly pass the key to be safe
)

# --- Create documents ---

# Create LangChain documents for IPL players

# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# --- Create vector store from documents (adds documents and builds embeddings) ---
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,          # pass the embeddings object
    persist_directory=PERSIST_DIR,
    collection_name=COLLECTION_NAME
)

# Step 4: Convert vectorstore into a retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

query = "What is Chroma used for?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)
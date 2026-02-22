# vector_stores.py
import os
import sys
import os
from dotenv import load_dotenv

load_dotenv()  # ← THIS loads .env variables into environment

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS


# --- CONFIG ---
# preferred model name for Gemini embeddings
EMBEDDING_MODEL = "models/gemini-embedding-001"
PERSIST_DIR = "maximal_marginal_relevance_db"
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


# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]



vectorStore=FAISS.from_documents(
    documents=docs,
    embedding=embeddings,          # pass the embeddings object
)

# Enable MMR in the retriever
retriever = vectorStore.as_retriever(
    search_type="mmr",                   # <-- This enables MMR
    search_kwargs={"k": 3, "lambda_mult": 0.5}  # k = top results, lambda_mult = relevance-diversity balance
)

query = "What is langchain?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

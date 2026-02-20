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
PERSIST_DIR = "my_chroma_db"
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

doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )
doc2 = Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"}
    )
doc3 = Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"}
    )
doc4 = Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"}
    )
doc5 = Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"}
    )
docs = [doc1, doc2, doc3, doc4, doc5]

# --- Create vector store from documents (adds documents and builds embeddings) ---
vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,          # pass the embeddings object
    persist_directory=PERSIST_DIR,
    collection_name=COLLECTION_NAME
)

print("✅ Documents embedded and stored to Chroma.")

# view documents
docsData=vector_store.get(include=['embeddings','documents', 'metadatas'])


# --- Querying the vector store ---

# search documents
players=vector_store.similarity_search(
    query='Who are the players from Mumbai Indians?',
    k=2  # number of results to return
)

print(players)

# search with metadata filter
data_with_scores=vector_store.similarity_search_with_score(
    query="Who are the players from Chennai Super Kings?",
    k=2
)

# print(data_with_scores)

# metadata filter without query
# meta-data filtering
# meta_filtered_data=vector_store.similarity_search(
 #   query="",
#    filter={"team": "Chennai Super Kings"},
 #   k=2
#)


# print(meta_filtered_data)


# update documents
updated_doc1 = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata={"team": "Royal Challengers Bangalore"}
)

vector_store.update_document(document_id='09a39dc6-3ba6-4ea7-927e-fdda591da5e4', document=updated_doc1)

# delete document
vector_store.delete(ids=['09a39dc6-3ba6-4ea7-927e-fdda591da5e4'])




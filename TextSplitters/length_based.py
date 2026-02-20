from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

load=PyPDFLoader('dl-curriculum.pdf')
docs=load.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator='\n'
)

result = splitter.split_documents(docs)
print(result[0])

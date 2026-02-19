from langchain_community.document_loaders import (
    PyPDFLoader,
    UnstructuredPDFLoader,
    PDFPlumberLoader,
    DirectoryLoader
)

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()  # returns a generator, not a list


for document in docs:
    print(document.metadata)

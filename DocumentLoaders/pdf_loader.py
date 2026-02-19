from langchain_community.document_loaders import (
    PyPDFLoader,
    UnstructuredPDFLoader,
    PDFPlumberLoader,
    PyMuPDFLoader,
)

from dotenv import load_dotenv
import os

load_dotenv()

loader2=PyMuPDFLoader("Appointment_Letter_Indranjana_Chatterjee.pdf")
docs2=loader2.load()


loader = PDFPlumberLoader("Appointment_Letter_Indranjana_Chatterjee.pdf")
docs = loader.load()

loader1 = UnstructuredPDFLoader(
    "Indranjana Chatterjee Resume.pdf",
    strategy="fast"
)
docs1 = loader1.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)

print(len(docs1))
print(docs1[0].page_content)

print(len(docs2))
print(docs2[0].page_content)

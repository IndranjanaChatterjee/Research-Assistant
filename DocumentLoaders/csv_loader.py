from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))

for doc in docs[:5]:  # Print the first 5 documents
    print(doc.page_content)
    print(doc.metadata) 

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import SystemMessage,HumanMessage
# chattemplate
chat_template=ChatPromptTemplate([
    ('system','you are a helpful customer support Agent?'),
    MessagesPlaceholder(variable_name='chat_history'),  # to retrieve and store the chat history before the human query so that context is maintained
    ('human','{query}')
])

chat_history=[]

# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
    


prompt=chat_template.invoke({'chat_history':chat_history,'query':HumanMessage(content='Where is my refund')})
print(prompt)
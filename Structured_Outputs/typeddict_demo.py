from typing import TypedDict

class Person(TypedDict):
    name:str
    number:int
    
new_Person:Person={'name':'Rohan','number':20}
print(new_Person)
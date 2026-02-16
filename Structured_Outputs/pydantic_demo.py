from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str
    surname:str='kumar' # setting default values which will always be shown either passed or not passed
    number:Optional[int]=None # optional field to be set exactly in this way
    email:EmailStr # built in in Pydantic which validates emails for correct email formats
    cgpa: Optional[float] = Field(default=None, gt=0, lt=10,description='A decimal value representing the cgpa marks') # Field helps to specify constraints

    
new_student={'name':'nitish','number':32,'email':'abc@gmail.com','cgpa':9}   # This will not take any other value of data type other than string and give errors
student = Student(**new_student)
print(student)
another_student={'name':'Roka','number':'75','email':'abc@gmail.com','cgpa':9.2} # number was suppose to be int , but PYDANTIC IS SMART ENOUGH TO UNDERSTAND THAT THE USER HAS PROVIDED A NUMBER ONLY BUT INS TRING FORMAT SO IT WILL PERFORM TYPE CONVERSION INTERNALLY AND MAKE IT INTERGER , THIS IS CALLED TYPE COERCION
stud=Student(**another_student)
print(stud)

stud_dict=dict(stud) #conversion to python dict
student_json=stud.model_dump_json()
print(stud_dict,' ',student_json)
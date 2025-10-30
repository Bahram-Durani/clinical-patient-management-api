
# Importing Pydantic base class for data validation

from pydantic import BaseModel, EmailStr  
from typing import List, Dict , Optional 

class Patient(BaseModel):  # Creating a data model using Pydantic
    name: str 
    age: int
    email: EmailStr   
    weight: float 
    married: Optional[bool]  = None 
    allergies: Optional[List[str]]   = None  # default value is None
    contact_details: Dict[str, str]      # key --> str,  value --> str 


def insert_patient_data(patient: Patient):  # Function that accepts an object
    print(patient.name)  
    print(patient.age) 
    print(patient.email)
    print(patient.weight)
    print(patient.married) 
    print(patient.allergies)  
    print('inserted')   


def update_patient_data(patient: Patient):  # Function that accepts an object
    print(patient.name) 
    print(patient.age) 
    print(patient.email)
    print(patient.weight)
    print(patient.married) 
    print(patient.allergies)
    print('updated')    


patient_data = {'name': 'Bahram', 'age': 24, 'email': 'xy@gmail.com', 'weight': 44.9, 'married': False, 
                'contact_details':  {'Email': 'bah13@gmail.com' , 'phone': '878734'} } 


patient1 = Patient(**patient_data)  # we write ** to unpack the dictionary  

# insert_patient_data(patient1)  # Passing validated data into function

update_patient_data(patient1)  # Passing validated data into function


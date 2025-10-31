from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    # keep your nice metadata
    name: Annotated[str, Field(
        max_length=50,  
        title='Name of the patient',
        description='Provide name of the patient in less than 50 chars',
        examples=['Nitish', 'Amit']
    )]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None,
                             description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)  # fixed attribute name
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)  # fixed attribute name
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print('updated')

patient_data = {
    'name': 'Bahram',
    'age': 24,
    'email': 'xy@gmail.com',
    'linkedin_url': 'https://www.linkedin.com/in/bahram',  # key fixed
    'weight': '98',   # will be coerced to float
    'married': False,
    'contact_details': {'Email': 'bah13@gmail.com', 'phone': '878734'}
    # 'allergies': ['penicillin']  # optional; add if you like (<= 5 items)
}

patient1 = Patient(**patient_data)

# insert_patient_data(patient1)
update_patient_data(patient1)

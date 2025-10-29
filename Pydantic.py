
# Importing Pydantic base class for data validation

from pydantic import BaseModel  # Basemodel checks for is data valid or not 

class Patient(BaseModel):  # Creating a data model using Pydantic
    name: str  #  name must be a string
    age: int   #  age must be an integer

def insert_patient_data(patient: Patient):  # Function that accepts an object
    print(patient.name)  # Accessing name from the Patient model
    print(patient.age)   # Accessing age from the Patient model
    print('inserted')    # Confirmation message


def update_patient_data(patient: Patient):  # Function that accepts an object
    print(patient.name)  # Accessing name from the Patient model
    print(patient.age)   # Accessing age from the Patient model
    print('updated')    # Confirmation message


patient_data = {'name': 'Bahram', 'age': 24}  # Raw input dictionary (like API input)
patient1 = Patient(**patient_data)  # we write ** to unpack the dictionary  

# insert_patient_data(patient1)  # Passing validated data into function

update_patient_data(patient1)  # Passing validated data into function


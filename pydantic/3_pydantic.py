# basic pydantic 

from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
   
patient_data = {
    "name": "John",
    "age": 30
}

patient = Patient(**patient_data) # creating object on dictionary

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted data into database")
    
insert_patient_data(patient)
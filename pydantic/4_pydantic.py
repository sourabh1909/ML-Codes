from pydantic import BaseModel
from typing import List  # for list of allergies
from typing import Dict  # for contact details

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]  # allergies is a list of strings
    contact: Dict
    
Patient_data = {
    "name": "John",
    "age": 30,
    "weight": 70.5,
    "married": True,
    "allergies": ["peanuts", "shellfish"],
    "contact": {
        "email": "abc@example.com",
        "phone": "1234567890"
    }
}

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print("inserted data into database")
    
patient = Patient(**Patient_data)
insert_patient_data(patient)

# agar hum koi bhi field ko skip karde to error throw hogi
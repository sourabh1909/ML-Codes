# this file is all about pydantic data validation by pydantic built in validators and custom validators
from pydantic import BaseModel
from typing import List  # for list of allergies
from typing import Dict  # for contact details
from typing import Optional  # for optional fields
from pydantic import EmailStr,AnyUrl

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedIn_url : AnyUrl
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None # allergies is a list of strings
    contact: Dict
# by assign operator we can set default value also for optional fields

Patient_data = {
    "name": "John",
    "age": 30,
    "email": "sourabhphalatane19@gmail.com",
    "linkedIn_url": "https://www.linkedin.com/in/sourabh-phalatane-9a1b4b1b6/",
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
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print("inserted data into database")
    
patient = Patient(**Patient_data)
insert_patient_data(patient)

# agar hum koi bhi field ko skip karde to error throw hogi
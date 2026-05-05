# by using one variable we can define another variable in pydantic

from pydantic import BaseModel,computed_field
from typing import Annotated, List  
from typing import Dict  
from typing import Optional  
from pydantic import EmailStr,AnyUrl,Field,field_validator,model_validator

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedIn_url : AnyUrl
    age: int
    weight:  float
    height: float
    allergies: Optional[List[str]]
    contact: Dict
    
    @computed_field #to take from user
    @property
    def cal_bmi(self) -> float:
        bmi = self.weight/ self.height ** 2
        return round(bmi, 2)

Patient_data = {
    "name": "John",
    "age": 30,
    "email": "sourabhphalatane19@hdfc.com",
    "linkedIn_url": "https://www.linkedin.com/in/sourabh-phalatane-9a1b4b1b6/",
    "weight": 70.5,
    "height": 1.75,
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
    print(patient.height)
    print(patient.cal_bmi)
    print(patient.allergies)
    print(patient.contact)
    print("inserted data into database")
    
patient = Patient(**Patient_data)  # here validation is performed

insert_patient_data(patient)

# field validators

from pydantic import BaseModel
from typing import Annotated, List  
from typing import Dict  
from typing import Optional  
from pydantic import EmailStr,AnyUrl,Field,field_validator,model_validator

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedIn_url : AnyUrl
    age: int
    weight:  Annotated[float,Field(gt=0,strict=True)]
    married: bool
    allergies: Optional[List[str]]
    contact: Dict

    @field_validator('email')
    @classmethod
    def email_validator(cla,value):
        valid_email = ['hdfc.com','sbi.com','icici.com']
        if not value.endswith("@hdfc.com"):
            raise ValueError("email must be from hdfc domain")
        # domain_name = value.split(@)[-1]
        # if domain_name not in valid_email:  
        #     raise ValueError("email must be from hdfc domain")
        else:
            return value
    # for single sinario
    @field_validator('name')
    @classmethod
    def tranform_name(cla,value):
        return value.upper()
    
    
    # @field_validator('age',mode='after')
    # @classmethod
    # def age_validator(cla,value):
    #     if 0 < value < 100:
    #         raise value
    #     else:
    #         return ValueError("age must be a positive integer")
    
# field validator operates in two ways before validation and after validation
    
    
    # for more than one validator
    @model_validator(mode='after')
    def validate_patient(cls, values):
        if values.age < 0 or values.age > 100:
            raise ValueError("age must be between 0 and 100")
        return values

Patient_data = {
    "name": "John",
    "age": 30,
    "email": "sourabhphalatane19@hdfc.com",
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
    
patient = Patient(**Patient_data)  # here validation is performed

insert_patient_data(patient)

# exporting this pydantic model to fastapi
from narwhals import exclude
from pydantic import BaseModel,computed_field


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name :str
    gender: str
    age: int
    address: Address
    
# pahle hame address model ke liye pydantic object banana padega
Address_data = {
    "city": "Pune",
    "state": "Maharashtra",
    "pin": "411001"
}

Address1 = Address(**Address_data) #unpacked

# ab hume patient model ke liye pydantic object banana hai
Patient_data ={
    "name": "Sourabh",
    "gender": "Male",
    "age": 30,
    "address": Address_data
}

Patient1 = Patient(**Patient_data) # unpacked

print(Patient1)
print(Patient1.name)
print(Patient1.address.city)



temp = Patient1.model_dump(include=['name', 'gender']) # to export in dict
# this model_dump() gives additional power
json_data = Patient1.model_dump_json() # to export in json


temp1 = Patient1.model_dump(exclude=['address', 'state']) # to export in dict

print(temp)
print(type(temp))

print(temp1)
print(type(temp))

# agar humane gender ki value default male hai to 
# hum exclude_unset = True use kar sakte hai to exclude the unset value from the output
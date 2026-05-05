# nested_model means one model is used inside another model
# agar data mai hirarchy hai to hum nested model use karte hai

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
print(Patient1)

# nested model is used to maintain the data integrity of the nested data structure

# better organization of related data(eg. address details) in a separate model
# reusability of the nested model in other models (eg. address model can be used in other models like doctor, hospital etc.)
# Readbility : Easier to develop and API consumer to understand
# validation : Nested models are validated automatically -no extra work needed
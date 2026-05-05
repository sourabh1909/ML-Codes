from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
   
# now we have to create an object of patient class

# pahle ek dictionary banate hai jisme patient ka data hoga
patient_data = {
    "name": "John",
    "age": 30
}

# ab hum patient object create karte hain
# here ** means that we are unpacking the dictionary and passing the values as arguments to the Patient class
patient = Patient(**patient_data)


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted data into database")
    
insert_patient_data(patient)

# age : '30' also be valid because pydantic will automatically convert the string to integer if possible
# type validation

def insert_patient_data(name,age): 
    print(name)
    print(age)
    print("inserted data into database")
    
# pyhton is dynamically types language
# we can change the datatype of variable when we give input
# but in real world application we need to maintain the data integrity

# so either we can use type hinting or we can use pydantic to maintain the data integrity

# type hinting is a way to specify the type of variable in python
def insert_patient_data_1(name: str, age: int):
    
    print(name)
    print(age)
    print("inserted data into database")
    
# but type hinting is not a strict way to maintain the data integrity
# we can still pass the wrong data type to the function and it will not raise any error

# therfore
def insert_patient_data_2(name: str, age: int):
    if type(name) == str and type(age) == int:
         print(name)
         print(age)
         print("inserted data into database")
    else:
        print("Invalid data type")
        
def update_patient_data_2(name: str, age: int):
    if type(name) == str and type(age) == int:
         print(name)
         print(age)
         print("updated data into database")
    else:
        print("Invalid data type")        
# this is one way to maintain the data integrity but it is not a good way

# 2. Data validation

#since pythan is dynamically typed landuage so data types are not specifically defined hence we use pydantic
# #give below is the method to make it validate with dtype but it is not scalable
# def insert_patient_data(name , age)


#not scalable because we have to creat the different funtion for tht update, delete,retrive
#type validation- like name cannot be in int thus we have to write the manual code  
#data validation- like age cannot be negative, for handling this again we have to add the if statment
# def insert_patient_data(name: str, age: int):
#     if type(name)==str and type(age)= int :
#         print(age, name)
#         print("insert the data")
#
#     else:
#         return TpyeError("Incorrect data type")
# insert_patient_data("nitesh", 30)


#defining the schemea 
from pydantic import BaseModel
class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient : Patient):# pyentic object is defined and passed
    print(patient.name)
    print(patient.age)

patients = [
    {
        "name": "Anuj",
        "age": 19
    },
    {
        "name": "Raghav",
        "age": 21
    }
]

for patient_data in patients:
    patient_object= Patient(**patient_data)
    insert_patient_data(patient_object)

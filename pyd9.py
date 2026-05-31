from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

#Serialization means converting a Python object into a format that can be stored, sent, or shared.
#Why use serialization?
#When you create a Pydantic object:
'''
Use serialization when data needs to go outside Python object form:
Python object → dict / JSON → API / file / database / frontend
'''
'''
Sending API response in FastAPI
Saving data into a file
Sending data to another service
Saving into a database
Hiding sensitive fields
Example: you do not want to send password or private contact details.
6. Sending only selected fields
Example: frontend only needs name and age.
Simple real-life example
Think of a Pydantic model like a student ID card object in Python.

But when you want to send it through WhatsApp, email, API, or save it in a file, you need to convert it into text/data format.

That conversion is serialization.
'''
# Nested model
class Address(BaseModel):
    city: str
    state: str
    country: str


# Main model
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    email: EmailStr
    allergies: List[str]
    address: Address
    contact_details: Dict[str, str]

    # computed_field is included during serialization
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)


# Input data as dictionary
patient_details = {
    "name": "Anuj",
    "age": 19,
    "weight": 78,
    "height": 1.75,
    "email": "anuj234@gmail.com",
    "allergies": ["dust", "pollen"],
    "address": {
        "city": "Mumbai",
        "state": "Maharashtra",
        "country": "India"
    },
    "contact_details": {
        "phone": "903839",
        "emergency_contact": "9876543210"
    }
}


# Creating Pydantic object
patient = Patient(**patient_details)


# 1. Normal object output
print("Pydantic object:")
print(patient)


# 2. Convert Pydantic object to Python dictionary
print("\nDictionary serialization:")
patient_dict = patient.model_dump()
print(patient_dict)


# 3. Convert Pydantic object to JSON string
print("\nJSON serialization:")
patient_json = patient.model_dump_json()
print(patient_json)


# 4. Serialize only selected fields
print("\nOnly selected fields:")
selected_data = patient.model_dump(include={"name", "age", "email"})
print(selected_data)


# 5. Exclude some fields during serialization
print("\nExclude some fields:")
without_contact = patient.model_dump(exclude={"contact_details"})
print(without_contact)


# 6. Serialize nested field also
print("\nOnly address field:")
address_data = patient.model_dump(include={"address"})
print(address_data)


# 7. Exclude unset values
# Useful when optional fields are not provided
print("\nExclude unset values:")
print(patient.model_dump(exclude_unset=True))


# 8. Convert JSON string back to Python dictionary
print("\nJSON string:")
print(patient.model_dump_json(indent=4))
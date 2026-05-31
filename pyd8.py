from pydantic import BaseModel
from typing import List, Dict, Annotated, Optional


class Address(BaseModel):
    city: str
    state: str
    country: str


address_details = {
    "city": "Mumbai",
    "state": "Maharastra",
    "country": "India"
}

address_object = Address(**address_details)


class Patient(BaseModel):
    name: str
    age: int
    addr: Address


patient_details = {
    "name": "anuj",
    "age": 19,
    "addr": address_object#this is important
}

patient_object = Patient(**patient_details)


def print_patient(patient: Patient):
    fields = ["name", "age", "addr"]

    #for i in fields:
    #   print(getattr(patient, i))
    print(patient.name)
    print(patient.age)
    print(patient.addr.city)
    print(patient.addr.state)
    print(patient.addr.country)
    

print_patient(patient_object)
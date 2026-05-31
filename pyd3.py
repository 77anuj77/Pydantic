from pydantic import BaseModel, EmailStr, AnyUrl#emailstr is used for yrname@gmail.com for sitpune@gmail.com we use fieldvalidator
from typing import List, Dict, Optional


#defining the schema with field type with optional
class Patient(BaseModel):
    name: str
    age: int#Pydantic automatic type conversion works for that we use feild and stict=true
    weight: float
    email:EmailStr
    url: AnyUrl
    married: bool=False
    alergies: Optional[List[str]]=None
    contact_details: Dict[str, str]=None
    
def insert_Patient_data(patient: Patient):
    fields = ["name", "age", "weight", "alergies", "contact_details", "married", "email", "url"]

    for i in fields:
        print(getattr(patient, i))

patient_detail = {
    "name": "anuj",
    "age": 19,
    "weight": 78,
    "alergies":[],
    "contact_details": {
        "email": "anuj.paroha@gmail.com",
        "phone": "903839"
    },
    "email": "anujparoha@fmail.com",
    "url":"http://linked.com/and"
}

patient_object = Patient(**patient_detail)
insert_Patient_data(patient_object)


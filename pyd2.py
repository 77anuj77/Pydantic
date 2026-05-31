from pydantic import BaseModel
from typing import List, Dict, Optional


#defining the schema with field type with optional
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool=False
    alergies: Optional[List[str]]=None
    contact_details: Dict[str, str]=None
    
def insert_Patient_data(patient: Patient):
    fields = ["name", "age", "weight", "alergies", "contact_details", "married"]

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
    }
}

patient_object = Patient(**patient_detail)
insert_Patient_data(patient_object)


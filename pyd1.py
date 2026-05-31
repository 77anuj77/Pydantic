from pydantic import BaseModel
from typing import List, Dict

#by defaut all fields must be filled
#defining the schema with field type
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    alergies: List[str]
    contact_details: Dict[str, str]
    
def insert_Patient_data(patient: Patient):
    fields = ["name", "age", "weight", "alergies", "contact_details"]

    for i in fields:
        print(getattr(patient, i))

patient_detail = {
    "name": "anuj",
    "age": 19,
    "weight": 78,
    "alergies": ["pollen", "dust"],
    "contact_details": {
        "email": "anuj.paroha@gmail.com",
        "phone": "903839"
    }
}

patient_object = Patient(**patient_detail)
insert_Patient_data(patient_object)


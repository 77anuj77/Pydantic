from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

#field not only used for the data type validation but also for description or metadata for developer in documentation
#defining the schema with field type with optional
class Patient(BaseModel):
    name: str=Field(max_length=50)
    age: int=Field(gt=0 , lt=50)
    weight: Annotated[float, Field(gt=10, title="name of the patient", description="name mist be have 10 words atleast", example=["anuj"])]
    email:EmailStr
    score:Annotated[int,Field(gt=0, strict=True)] #strict= True means no type conversion automatically by pydantic 
    url: AnyUrl
    married: bool=False
    alergies: Annotated[Optional[List[str]],Field(max_length=5, title="alergies", description="pass the alergies", examples=["cold", "dust"])]=None
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


from pydantic import BaseModel,EmailStr,AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional

#when our work is to check the condition afecting the two or more field then we apply model_validator
#model_validator work is to get the data_validation in two or more fields
#we can do data_validation by combinng two or more field
class Patient(BaseModel): 
    email: EmailStr
    url: AnyUrl
    name: str
    age: int
    weight: float
    married: bool=False
    alergies: Optional[List[str]]
    contact_details: Dict[str, str]

    '''mole_validator for only accepting the persor with age gt=40 must hve the emergency contact detail'''
    @model_validator(mode='after')
    def age_emergency_validator(cls, model):#we are passing the class and the model since we have to apply for all field
        if model.age>=40 and "phone" not in model.contact_details:
            raise ValueError("you must fill the contact")
        else:
            return model
        

def insert_Patient_data(patient: Patient):
    fields = ["email","url","name", "age", "weight", "alergies", "contact_details", "married"]
 
    for i in fields:
        print(getattr(patient, i))

#actually what happens pydantic converts the datatype automatically like if we have string->>'23572958' then this will be converted to int automatically if in chema its is defined as int
#thus we use two mode in validator mode= before and after
#if mode= before ->> it means befor etype validation 
patient_detail = {
    "email": "anuj@icici.com",
    "url": "https://example.com",
    "name": "anuj",
    "age": '50',
    "weight": '78',
    "alergies":[],
    "contact_details": {
        "email": "anuj.paroha@gmail.com",
        "phone": "903839"
    }
}

patient_object = Patient(**patient_detail)
insert_Patient_data(patient_object)


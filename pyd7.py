from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Annotated, Optional

#computed fiels are used for extracting the other fields which the user cannot provide like BMI using height, weight fields

class Patient(BaseModel):
    email: EmailStr
    age: Annotated[Optional[int], Field(gt=0, title="The age of the patient", description="Must me greater than zero", examples=[34,22,34])]=18
    weight: int=Field(gt=5)
    height: int=Field(gt=0)
    married: bool=None
    allergies: List[str]
    contact_details: Dict[str, str]

    #so technically the name of the functions is treated as the field name
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi=round((self.weight/self.height*100), 2)
        return bmi
        



patient_details={
    "email":"anuj234@gmail.com",
    "age": 34,
    "weight": 64,
    "height": 175,
    "married": True,
    "allergies": ['Dust', "cold"],
    "contact_details":{
        "phone":"90349093",
        "email":"anuj1234@gmail.com"
    }
}

def insert_patient_details(patient: Patient):
    fields=["email", "age", "weight", "height", "married", "allergies","contact_details", "calculate_bmi"]#instead of passing the bmi -->> calculate_bmi
    for i in fields:
        print(getattr(patient, i))

object_patient= Patient(**patient_details)
insert_patient_details(object_patient)
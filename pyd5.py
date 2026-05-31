from pydantic import BaseModel,EmailStr,AnyUrl, Field, field_validator
from typing import List, Dict, Optional

#field_validatotor is used for customising the field
#let suppose we have to check whether the email is of the particular organisation or not
#for example we are taking the domain icici.com and hdfc.com
#for this we have to make a new method inside the class 

class Patient(BaseModel): 
    email: EmailStr
    url: AnyUrl
    name: str
    age: int
    weight: float
    married: bool=False
    alergies: Optional[List[str]]
    contact_details: Dict[str, str]

    #email_validator
    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domains=["hdfc.com", "icici.com"]
        domain_name=value.split("@")[-1]

        if domain_name in valid_domains:
            return value
        else:
            raise ValueError("this is not the valid domain")
        
    #age validator without using field()
    @field_validator("age", mode='after')#because before me error aagaya
    @classmethod
    def age_validator(cls, value):
        if 0< value< 100:
            return value
        else:
            raise ValueError("age is not ok")
        

    #string_validatotr
    @field_validator("name")
    @classmethod
    #str.capitalize(): Capitalizes the first letter of the entire string and converts all other characters to lowercase (e.g., "hello WORLD" becomes "Hello world"). 
    #str.title(): Capitalizes the first letter of every word and lowercases the rest (e.g., "hello WORLD" becomes "Hello World")
    #str.upper(): whole string is in capital letters
    #Slicing (text[0].upper() + text[1:]): Only affects the first character, preserving the case of the remaining characters.
    def string_validator(cls, value):
        return value.title()


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
    "age": '19',
    "weight": '78',
    "alergies":[],
    "contact_details": {
        "email": "anuj.paroha@gmail.com",
        "phone": "903839"
    }
}

patient_object = Patient(**patient_detail)
insert_Patient_data(patient_object)


from pydantic import BaseModel

class InputContact(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
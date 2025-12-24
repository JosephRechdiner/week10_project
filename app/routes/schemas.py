from pydantic import BaseModel
from typing import Optional
class CreateContact(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

class UpdateContact(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
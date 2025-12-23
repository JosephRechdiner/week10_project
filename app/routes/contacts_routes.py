from fastapi import APIRouter, Depends
from mysql.connector import connection
from database.create_connection import get_connection
from service import contact_service
from routes.schemas import InputContact
from database.contact_model import Contact

contact_router = APIRouter(prefix="/contancts")

@contact_router.get("/get_contacts")
def get_all_contacts(conn: connection = Depends(get_connection)):
    return contact_service.list_contacts(conn)

@contact_router.post("/add_contact")
def add_one_contact(contact: InputContact, conn: connection = Depends(get_connection)):
    return contact_service.add_contact(contact.first_name, contact.last_name, contact.phone_number, conn)

@contact_router.put("/update_contact{id}")
def update_contact_by_id(id: int, contact: InputContact, conn: connection = Depends(get_connection)):
    return contact_service.update_contact_info(id, contact.first_name, contact.last_name, contact.phone_number, conn)

@contact_router.delete("/delete_contact/{id}")
def delete_contact_by_id(id: int, conn: connection = Depends(get_connection)):
    return contact_service.remove_contact(id, conn)
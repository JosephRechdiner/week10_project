from fastapi import APIRouter, Depends
from mysql.connector import connection
from app.database.data_interactor import get_connection
from service.contact_service import ServiceManager
from routes.schemas import CreateContact, UpdateContact

contact_router = APIRouter(prefix="/contacts")

@contact_router.get("/get_contacts")
def get_all_contacts(conn: connection = Depends(get_connection)):
    return ServiceManager.list_contacts(conn)

@contact_router.post("/add_contact")
def add_one_contact(contact: CreateContact, conn: connection = Depends(get_connection)):
    return ServiceManager.add_contact(contact.model_dump(), conn)

@contact_router.put("/update_contact/{id}")
def update_contact_by_id(id: int, contact: UpdateContact, conn: connection = Depends(get_connection)):
    return ServiceManager.update_contact_info(id, contact.model_dump(), conn)

@contact_router.delete("/delete_contact/{id}")
def delete_contact_by_id(id: int, conn: connection = Depends(get_connection)):
    return ServiceManager.remove_contact(id, conn)
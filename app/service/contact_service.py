from mysql.connector import connection
from dal import contact_dal
from fastapi import HTTPException


def list_contacts(conn: connection):
    data = contact_dal.get_all_contacts(conn)
    if not data:
        return {"messege", "No contacts in DB"}
    return data


def add_contact(first_name: str, last_name: str, phone_number: str, conn: connection):
    try:
        contact_id = contact_dal.create_contact(first_name, last_name, phone_number, conn)
        return {"messege": "Contact created succesfully", "Id": contact_id}
    except:
        raise HTTPException(status_code=409, detail="Could not access DB")


def update_contact_info(id: int, first_name: str, last_name: str, phone_number: str, conn: connection):
    try:
        has_updated = contact_dal.update_contact(id, first_name, last_name, phone_number, conn)
        if has_updated:
            return {"messege": "Contact updated succesfully"}
        raise
    except:
        raise HTTPException(status_code=404, detail="Contact not found")


def remove_contact(id: int, conn: connection):
    try:
        has_deleted = contact_dal.delete_contact(id, conn)
        if has_deleted:
            return {"messege": "Contact deleted succesfully"}
        raise
    except:
        raise HTTPException(status_code=404, detail="Contact not found")
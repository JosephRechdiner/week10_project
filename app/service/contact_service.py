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
        return {"msg": "Contact created succesfully", "ID": contact_id}
    except Exception as e:
        raise HTTPException(status_code=409, detail=e)

def update_contact_info(first_name: str, last_name: str, phone_number: str, conn: connection):
    try:
        has_updated = contact_dal.update_contact(first_name, last_name, phone_number, conn)
        if has_updated:
            return {"msg": "Contact updated succesfully"}
        raise HTTPException(status_code=404, detail="Contact not found")
    except Exception as e:
        raise HTTPException(status_code=409, detail=e)


def remove_contact(first_name: str, last_name: str, phone_number: str, conn: connection):
    try:
        has_deleted = contact_dal.update_contact(first_name, last_name, phone_number, conn)
        if has_deleted:
            return {"msg": "Contact deleted succesfully"}
        raise HTTPException(status_code=404, detail="Contact not found")
    except Exception as e:
        raise HTTPException(status_code=409, detail=e)
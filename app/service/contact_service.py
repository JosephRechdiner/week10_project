from mysql.connector import connection
from dal.contact_dal import DalManager
from fastapi import HTTPException

class ServiceManager:
    def list_contacts(conn: connection):
        data = DalManager.get_all_contacts(conn)
        if not data:
            return {"messege", "No contacts in DB"}
        return data


    def add_contact(contact: dict, conn: connection):
        try:
            contact_id = DalManager.create_contact(contact, conn)
            return {"messege": "Contact created succesfully", "Id": contact_id}
        except:
            raise HTTPException(status_code=409, detail="Could not access DB")


    def update_contact_info(id: int, contact: dict, conn: connection):
        try:
            has_updated = DalManager.update_contact(id, contact, conn)
            if has_updated:
                return {"messege": "Contact updated succesfully"}
            raise
        except:
            raise HTTPException(status_code=404, detail="Contact not found")


    def remove_contact(id: int, conn: connection):
        try:
            has_deleted = DalManager.delete_contact(id, conn)
            if has_deleted:
                return {"messege": "Contact deleted succesfully"}
            raise
        except:
            raise HTTPException(status_code=404, detail="Contact not found")
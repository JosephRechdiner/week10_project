from mysql.connector import connection
from dal.contact_dal import DalManager
from fastapi import HTTPException

class ServiceManager:
    @staticmethod
    def list_contacts(conn: connection):
        data = DalManager.get_all_contacts(conn)
        if not data:
            return {"messege": "No contacts in DB"}
        return data

    @staticmethod
    def add_contact(contact: dict, conn: connection):
        try:
            contact_id = DalManager.create_contact(contact, conn)
            return {"messege": "Contact created succesfully", "Id": contact_id}
        except Exception as e:
            raise HTTPException(status_code=409, detail=str(e))

    @staticmethod
    def update_contact_info(id: int, contact: dict, conn: connection):
        try:
            has_updated = DalManager.update_contact(id, contact, conn)
            if not has_updated:
                raise HTTPException(status_code=404, detail="Contact not found")
            return {"messege": "Contact updated succesfully"}
        except Exception as e:
            raise HTTPException(status_code=409, detail=str(e))

    @staticmethod
    def remove_contact(id: int, conn: connection):
        try:
            has_deleted = DalManager.delete_contact(id, conn)
            if not has_deleted:
                raise HTTPException(status_code=404, detail="Contact not found")
            return {"messege": "Contact deleted succesfully"}
        except Exception as e:
            raise HTTPException(status_code=409, detail=str(e))
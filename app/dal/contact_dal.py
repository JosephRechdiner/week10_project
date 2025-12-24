from mysql.connector import connection
from utils import convert_db_to_objects

class DalManager:
    @staticmethod
    def get_all_contacts(conn: connection):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts;")
        rows = cursor.fetchall()

        if not rows:
            return False 

        data = convert_db_to_objects(rows) 
        cursor.close()
        return data

    @staticmethod
    def create_contact(contact: dict, conn: connection):
        cursor = conn.cursor()
        try: 
            cursor.execute(
                "INSERT INTO contacts (first_name, last_name, phone_number) " \
                "VALUES(%s, %s, %s);",(
                    contact["first_name"],
                    contact["last_name"],
                    contact["phone_number"],
                    )
                )
            contact_id = cursor.lastrowid
            conn.commit()
            return contact_id
        
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()

    @staticmethod
    def update_contact(id: int, contact: dict, conn: connection):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM contacts WHERE id = %s;", (id,))
            contact_to_update = cursor.fetchone()
            if not contact_to_update:
                return False
            
            for key, val in contact.items():
                if val is not None:
                    query = f'UPDATE contacts SET `{key}` = %s WHERE id = %s;'
                    cursor.execute(query, (val, id,))

            conn.commit()
            return True

        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()

    @staticmethod
    def delete_contact(id: int, conn: connection):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM contacts WHERE id = %s;", (id,))
            user_to_delete = cursor.fetchone()
            if not user_to_delete:
                return False

            cursor.execute("DELETE FROM contacts WHERE id = %s;",(id,))
            conn.commit()
            return True

        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
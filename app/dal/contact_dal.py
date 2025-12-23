from mysql.connector import connection
from utils import convert_db_to_objects


def get_all_contacts(conn: connection):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts;")
    rows = cursor.fetchall()

    if not rows:
        return False 

    data = convert_db_to_objects(rows) 
    cursor.close()
    conn.close()
    return data


def create_contact(first_name: str, last_name: str, phone_number: str, conn: connection):
    cursor = conn.cursor()
    try: 
        cursor.execute(
            "INSERT INTO contacts (first_name, last_name, phone_number) " \
            "VALUES(%s, %s, %s);",(
                first_name,
                last_name,
                phone_number,
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


def update_contact(id: int, first_name: str, last_name: str, phone_number: str, conn: connection):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM contacts WHERE id = %s;", (id,))
        user_to_update = cursor.fetchone()
        if not user_to_update:
            return False

        cursor.execute(
        "UPDATE contacts " \
        "SET first_name = %s, last_name = %s, phone_number = %s WHERE id = %s;",(
                first_name,
                last_name,
                phone_number,
                id)
            )
        conn.commit()
        return True

    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()


def delete_contact(id: int, conn: connection):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM contacts WHERE id = %s;", (id,))
        user_to_delete = cursor.fetchone()
        if not user_to_delete:
            return False

        cursor.execute(
        "DELETE FROM contacts WHERE id = %s;",(id,))
        conn.commit()
        return True

    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
from app.database.contact_model import Contact

def load_sql(path):
    try:
        with open(path, "r") as file:
            file_script = file.read()
            return file_script
    except Exception as e:
        return {"Error": e}
    
def convert_db_to_objects(rows):
    objects = []
    for row in rows:
        new_contact = Contact(
            first_name=row[0],
            last_name=row[1],
            phone_number=row[2]
            )
        objects.append(new_contact)
    return objects
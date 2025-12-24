from database.contact_model import Contact
    
def convert_db_to_objects(rows):
    objects = []
    for row in rows:
        new_contact = Contact(
            id=row[0],
            first_name=row[1],
            last_name=row[2],
            phone_number=row[3]
            )
        objects.append(new_contact)
    return objects
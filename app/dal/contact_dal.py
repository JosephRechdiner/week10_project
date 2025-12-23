from fastapi import Depends, HTTPException
from database.create_connection import get_connection
from mysql.connector import connection

def get_all_contacts(conn: connection = Depends(get_connection)):
    pass

def create_contact():
    pass

def update_contact():
    pass

def delete_contact():
    pass

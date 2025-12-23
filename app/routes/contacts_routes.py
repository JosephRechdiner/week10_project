from fastapi import APIRouter, Depends

contact_router = APIRouter(prefix="/contanct")

@contact_router.get("/")
def home(conn: connection = Depends(get_connection)):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts; ")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        cur_row = {}
        cur_row["First name"] = row[0]
        cur_row["Last name"] = row[1]
        cur_row["Phone number"] = row[2]
        
        data.append(cur_row)
    cursor.close()
    conn.close()
    return {"data": data}
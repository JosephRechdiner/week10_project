from fastapi import FastAPI
from routes.contacts_routes import contact_router

app = FastAPI()

app.include_router(contact_router)
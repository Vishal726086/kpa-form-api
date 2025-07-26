from fastapi import FastAPI
from app.routers import form_data

app = FastAPI()

app.include_router(form_data.router)


# for temporary
from app.database import Base, engine
from app.models import FormData

Base.metadata.create_all(bind=engine)

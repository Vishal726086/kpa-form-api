from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter(
    prefix="/form-data",
    tags=["Form Data"]
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST: /form-data/submit
@router.post("/submit", response_model=schemas.FormDataOut)
def submit_form(form: schemas.FormDataCreate, db: Session = Depends(get_db)):
    form_data = models.FormData(**form.dict())
    db.add(form_data)
    db.commit()
    db.refresh(form_data)
    return form_data

# GET: /form-data/{id}
@router.get("/{id}", response_model=schemas.FormDataOut)
def get_form_data(id: int, db: Session = Depends(get_db)):
    form_data = db.query(models.FormData).filter(models.FormData.id == id).first()
    if not form_data:
        raise HTTPException(status_code=404, detail="Form data not found")
    return form_data

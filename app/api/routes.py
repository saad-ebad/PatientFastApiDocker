from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db
from typing import List

router = APIRouter()

@router.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_patient = crud.get_patient_by_email(db, email=patient.email)
    if db_patient:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_patient(db=db, patient=patient)

@router.get("/patients/{patient_id}", response_model=schemas.Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud.get_patient(db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@router.put("/patients/{patient_id}", response_model=schemas.Patient)
def update_patient(patient_id: int, patient: schemas.PatientUpdate, db: Session = Depends(get_db)):
    db_patient = crud.get_patient(db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return crud.update_patient(db=db, patient_id=patient_id, patient=patient)

@router.delete("/patients/{patient_id}", response_model=schemas.Patient)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud.get_patient(db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return crud.delete_patient(db=db, patient_id=patient_id)

@router.get("/patients/", response_model=List[schemas.Patient])
def read_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    patients = crud.get_patients(db, skip=skip, limit=limit)
    return patients
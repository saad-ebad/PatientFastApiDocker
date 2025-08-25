from pydantic import BaseModel
from typing import List, Optional

class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    email: str  # Add this line
    address: str  # Keep this if you want it
    diagnosis: Optional[str] = None  # Add this if you want diagnosis

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    email: Optional[str] = None  # Add this
    address: Optional[str] = None
    diagnosis: Optional[str] = None  # Add this

class PatientList(BaseModel):
    patients: List[Patient]
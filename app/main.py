from fastapi import FastAPI
from app.api.routes import router as patients_router
from app.database import engine
from app.models import Base

app = FastAPI()

# Create the database tables
@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

# Include the router for patient operations
app.include_router(patients_router, prefix="/patients", tags=["patients"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Patients CRUD API"}
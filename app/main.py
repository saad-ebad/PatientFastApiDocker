import os
import uvicorn
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

# ✅ Run Uvicorn programmatically, picking PORT from environment (Railway sets it automatically)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # default to 8000 if not set
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)

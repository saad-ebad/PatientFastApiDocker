from sqlalchemy import Column, Integer, String, Sequence
from app.database import Base

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, Sequence('patient_id_seq'), primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    diagnosis = Column(String(255), nullable=True)
    address = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<Patient(name={self.name}, age={self.age}, gender={self.gender}, email={self.email}, diagnosis={self.diagnosis})>"

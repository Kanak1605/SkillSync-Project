from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app import models, schemas
import json
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
def create_user(db: Session, user: schemas.UserCreate):
    hashed = pwd_context.hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed, full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not pwd_context.verify(password, user.hashed_password):
        return None
    return user
def create_resume(db: Session, owner_id: int, filename: str, raw_text: str, parsed_obj: dict):
    r = models.Resume(filename=filename, raw_text=raw_text, parsed_json=json.dumps(parsed_obj), owner_id=owner_id)
    db.add(r)
    db.commit()
    db.refresh(r)
    return r
def get_resume(db: Session, resume_id: int):
    return db.query(models.Resume).filter(models.Resume.id == resume_id).first()
def create_job(db: Session, job_in: schemas.JobCreate):
    job = models.Job(title=job_in.title, description=job_in.description, requirements=job_in.requirements)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job
def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()
def list_resumes(db: Session):
    return db.query(models.Resume).all()

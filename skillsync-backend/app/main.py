from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api import auth, resumes, jobs
Base.metadata.create_all(bind=engine)
app = FastAPI(title="SkillSync Backend")
app.include_router(auth.router)
app.include_router(resumes.router)
app.include_router(jobs.router)
@app.get("/")
def root():
    return {"app": "skillsync backend", "status": "ok"}

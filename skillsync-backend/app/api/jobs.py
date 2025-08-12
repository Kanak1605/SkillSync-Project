from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app import crud, schemas
from app.matching.tfidf_matcher import rank_resumes_for_job
router = APIRouter(prefix="/jobs", tags=["jobs"])
@router.post("/", response_model=schemas.JobOut)
def create_job(job_in: schemas.JobCreate, db: Session = Depends(get_db)):
    job = crud.create_job(db, job_in)
    return job
@router.get("/{job_id}", response_model=schemas.JobOut)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
@router.get("/{job_id}/recommendations")
def job_recommendations(job_id: int, db: Session = Depends(get_db), top_k: int = 10):
    job = crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    resumes = crud.list_resumes(db)
    recs = rank_resumes_for_job(job.description + " " + (job.requirements or ""), resumes, top_k=top_k)
    return {"job_id": job.id, "recommendations": recs}

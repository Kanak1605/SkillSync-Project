from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import shutil, uuid, os
from app.db.session import get_db
from app import crud
from app.utils import parser
router = APIRouter(prefix="/resumes", tags=["resumes"])
UPLOAD_DIR = "/usr/src/app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
def get_current_user_fake():
    # placeholder, returns user id 1 for quick testing
    return 1
@router.post("/upload")
async def upload_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
    current_user = get_current_user_fake()
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    raw_text = parser.extract_text_from_file(filepath)
    parsed = parser.parse_resume_text(raw_text)
    resume = crud.create_resume(db, owner_id=current_user, filename=filename, raw_text=raw_text, parsed_obj=parsed)
    return {"resume_id": resume.id, "parsed": parsed}
@router.get("/{resume_id}")
def get_resume(resume_id: int, db: Session = Depends(get_db)):
    r = crud.get_resume(db, resume_id)
    if not r:
        raise HTTPException(status_code=404, detail="Resume not found")
    return r

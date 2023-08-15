from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from . import models, utils
import database
logs_router = APIRouter()

@logs_router.post("/upload")
def upload_logs(file: UploadFile = File(...), db: Session = Depends(database.get_db)):
    file_path = utils.save_uploaded_file(file)
    # Assuming logs are stored as plain text lines in the file
    with open(file_path, "r") as f:
        for line in f:
            log_entry = models.LogEntry(message=line.strip())
            db.add(log_entry)
        db.commit()
    return {"message": "Logs uploaded successfully"}

@logs_router.get("/logs")
def get_logs(
    start_date: str = None,
    end_date: str = None,
    keyword: str = None,
    db: Session = Depends(database.get_db)
):
    query = db.query(models.LogEntry)

    if start_date:
        query = query.filter(models.LogEntry.timestamp >= start_date)
    if end_date:
        query = query.filter(models.LogEntry.timestamp <= end_date)
    if keyword:
        query = query.filter(models.LogEntry.message.contains(keyword))

    logs = query.all()
    return logs

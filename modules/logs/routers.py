import zipfile
import io

from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from modules.database import get_db
from .models import LogEntry
from .utils import save_uploaded_file

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

logs_router = APIRouter()


@logs_router.post("/upload")
def upload_logs(
    token: Annotated[str, Depends(oauth2_scheme)],
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    if file.content_type != "application/zip":
        file_path = save_uploaded_file(file)
    # Assuming logs are stored as plain text lines in the file
        with open(file_path, "r") as f:
            for line in f:
                log_entry = LogEntry(message=line.strip())
                db.add(log_entry)
            db.commit()
        return {"message": "Logs uploaded successfully"}

    # Extract files from the uploaded ZIP archive
    zip_file_content = io.BytesIO(file.file.read())

    # Extract files from the uploaded ZIP archive
    with zipfile.ZipFile(zip_file_content, "r") as zip_ref:
        extracted_files = []
        for zip_info in zip_ref.infolist():
            if not zip_info.filename.endswith('/') and (zip_info.filename.endswith('.log') or zip_info.filename.endswith('.txt')):
                extracted_files.append(zip_info.filename)
                log_data = zip_ref.read(zip_info.filename).decode("utf-8")
                with io.StringIO(log_data) as log_stream:
                    for line in log_stream:
                        log_entry = LogEntry(message=line.strip())
                        db.add(log_entry)
        db.commit()

    return {"message": f"Logs uploaded from {len(extracted_files)} log files in the ZIP archive"}




@logs_router.get("/")
def get_logs(
    token: Annotated[str, Depends(oauth2_scheme)],
    start_date: str = None,
    end_date: str = None,
    keyword: str = None,
    db: Session = Depends(get_db),
):
    query = db.query(LogEntry)

    if start_date:
        query = query.filter(LogEntry.timestamp >= start_date)
    if end_date:
        query = query.filter(LogEntry.timestamp <= end_date)
    if keyword:
        query = query.filter(LogEntry.message.contains(keyword))

    logs = query.all()
    return logs

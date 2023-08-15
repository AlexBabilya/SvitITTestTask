import os
from werkzeug.utils import secure_filename
from zipfile import ZipFile
from fastapi import UploadFile

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'zip'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_file(file: UploadFile):
    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        with open(file_path, 'wb') as f:
            f.write(file.file.read())
        if filename.endswith('.zip'):
            with ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(UPLOAD_FOLDER)
        return file_path

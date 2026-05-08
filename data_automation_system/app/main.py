from fastapi import FastAPI, UploadFile, File
import shutil
import os
from .processor import process_data

app = FastAPI()

# Ensure directories exist
UPLOAD_DIR = "data/uploads"
REPORT_DIR = "reports/static"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

@app.post("/upload-analysis/")
async def upload_file(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Trigger the processing engine
    results = process_data(file_path, REPORT_DIR)
    
    return {
        "filename": file.filename,
        "results": results
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
from app.Data_Base.WorkDB import WorkDB
from typing import List
import os
import uvicorn
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

app = FastAPI(title="Save Foto API")

# Пути
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
DB_PATH = os.path.join(BASE_DIR, "Data_Base", "base_foto.db")

# Инициализация БД
db = WorkDB(DB_PATH, echo=False)

# Создаём папку для загрузок, если не существует
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...), name_dir: str = Form(...)):
    """Загрузка файлов на сервер."""
    
    # Создаем папку с указанным именем
    upload_path = os.path.join(UPLOAD_DIR, name_dir)
    os.makedirs(upload_path, exist_ok=True)

    uploaded_files = []
    
    for file in files:
        if not file.filename:
            continue
            
        file_content = await file.read()
        file_name = file.filename
        file_path = os.path.join(upload_path, file_name)

        # Сохраняем файл
        with open(file_path, "wb") as f:
            f.write(file_content)

        # Запись в БД
        foto = db.add_foto(name_foto=file_name, path=file_path)
        uploaded_files.append({
            "name": file_name,
            "path": file_path,
            "db_id": foto.id
        })

    return JSONResponse(
        status_code=200,
        content={"message": "Файлы успешно загружены", "files": uploaded_files}
    )


@app.get("/")
async def read_root():
    """Возвращает главную страницу."""
    index_path = os.path.join(os.path.dirname(__file__), "index.html")
    return FileResponse(index_path)


@app.get("/health")
async def health_check():
    """Проверка работоспособности API."""
    return {"status": "ok", "message": "API работает"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

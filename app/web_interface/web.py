from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from app.Data_Base.connectDB import Get_engine_session_DB
from app.Data_Base.model import Foto
from typing import List
import os
import uvicorn

app = FastAPI()

# Папка для загрузки файлов
UPLOAD_DIR = "uploads"

@app.post("/upload")
def root(files: List[UploadFile] = File(...),
         name_dir: str = Form(...)):
    
    # Создаем папку с указанным именем
    upload_path = os.path.join(UPLOAD_DIR, name_dir)
    os.makedirs(upload_path, exist_ok=True)
    
    # работа с БД
    connectDB = Get_engine_session_DB('../app/Data_Base/base_foto.db')
    engine = connectDB.get_engine()
    session = connectDB.get_sessoin()   

    # работа с файлами
    for file in files:
        file_content = file.file.read()
        file_name = file.filename
        path = f"{upload_path}/{file_name}"

        if not file_name:
            continue
        with open(path, "wb") as f:
            f.write(file_content)

        # запись в БД
        foto = Foto(name_foto=file_name, path=path)
        session.add(foto)
        session.commit()


@app.get("/")
def read_root():

    return FileResponse("index.html")

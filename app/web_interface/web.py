from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from app.database.SQL_request import *
from app.database.Connection import connection
from typing import List
from .functions.save_file import save_file
import os

app = FastAPI()


@app.post("/upload")
def root(folder: str = Form(...), files: List[UploadFile] = File(...)):
    db_conn = connection()
    name_colum = ["name_image"]
    get_query = SQL_request("table_image", name_colum).req_obtain()
    name_dict = db_conn.get_data(get_query)
    name_colum_path = ["path_flash_disk"]
    dir_path = SQL_request("path_flash_disk", name_colum_path).limited()
    get_path = db_conn.get_data(dir_path)
    dpath = ''

    for item in get_path:
        dpath = item
    for file in files:
        file_content = file.file.read()
        file_name = file.filename
        path_dir = f"{dpath}/{folder}"
        path = f"{path_dir}/{file_name}"
        if not os.path.exists(path_dir) or not os.path.isdir(path_dir):
            os.mkdir(path_dir)
        save_file(db_conn, file_content, file_name, path, name_dict)

    db_conn.close_DB()


@app.get("/")
def read_root():
    return FileResponse("../Project_1_Save_foto/app/web_interface/index.html")

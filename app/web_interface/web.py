from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from app.database.SQL_request import *
from app.database.Connection import connection
from typing import List
from app.web_interface.functions.save_file import save_file

app = FastAPI()


@app.post("/file")
def root(files: List[UploadFile] = File(...)):
    db_conn = connection()
    name_colum = ["name_image"]
    get_query = SQL_request("images", name_colum).req_obtain()
    name_dict = db_conn.get_data(get_query)

    for file in files:
        file_content = file.file.read()
        file_name = file.filename
        path = f"images/{file_name}"
        save_file(db_conn, file_content, file_name, path, name_dict)

    db_conn.close_DB()


@app.get("/")
def read_root():
    return FileResponse("index.html")

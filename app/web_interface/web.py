from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from database.SQL_request import *
from database.Connection import connection
from typing import List
import uvicorn

app = FastAPI()


@app.post("/file")
def root(files: List[UploadFile] = File(...)):
    table_images = connection()
    name_colum = ["name_image"]
    get_query = SQL_request("images", name_colum).req_obtain()
    name_dict = table_images.get_data(get_query)

    for file in files:
        file_content = file.file.read()
        file_name = file.filename
        path = f"images/{file_name}"
        if file_name in name_dict.keys():
            continue
        if not file_name:
            continue
        with open(path, "wb") as f:
            f.write(file_content)
        name_colums = ["name_image", "path"]
        values = [file_name, path]

        Query = SQL_request("images", name_colums, values)

        insert_query_sql = Query.req_insert()
        insert_query_values = Query.dict_values()

        table_images.perform_sql(insert_query_sql, insert_query_values)

    table_images.close_DB()


@app.get("/")
def read_root():
    return FileResponse("index.html")

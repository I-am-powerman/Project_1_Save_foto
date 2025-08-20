from app.database.SQL_request import SQL_request

def save_file(db_conn, file_content, file_name, path, name_dict):
        if file_name in name_dict.keys():
            return
        if not file_name:
            return
        with open(path, "wb") as f:
            f.write(file_content)
        name_colums = ["name_image", "path"]
        values = [file_name, path]

        Query = SQL_request("images", name_colums, values)

        insert_query_sql = Query.req_insert()
        insert_query_values = Query.dict_values()

        db_conn.perform_sql(insert_query_sql, insert_query_values)
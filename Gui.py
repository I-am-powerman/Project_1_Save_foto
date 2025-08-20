from tkinter import *
from tkinter import ttk
from app.gui.functions.loc_ip import loc_ip
from app.gui.functions.get_name_disk import get_name_disk
from app.database.SQL_request import *
from app.database.Connection import connection
import uvicorn
import os


root = Tk()
root.title("Save you foto")
root.geometry("270x500+200+100")

def selected(event):
    selection = combobox.get()
    db_conn = connection()
    name_colums = ["path_flash_disk"]
    values = [f"{path}/{selection}"]
    
    Query = SQL_request("path_flash_disk", name_colums, values)
    
    insert_query_sql = Query.req_insert()
    insert_query_values = Query.dict_values()

    db_conn.perform_sql(insert_query_sql, insert_query_values)
    db_conn.close_DB()


# виджеты
current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, "app/gui/favicon_2.png")
icon = PhotoImage(file=icon_path)
label_icon = ttk.Label(image=icon)
label_icon.pack()

label_ip = ttk.Label(text="Ваш IP:")
label_ip.pack()
message = StringVar(value=loc_ip())
entry_ip = ttk.Entry(textvariable=message)
entry_ip.pack(fill=X, pady = 10)

label_disk = ttk.Label(text="Выбор диска:")
label_disk.pack()
[values, path] = get_name_disk()
combobox = ttk.Combobox(values=values, justify=CENTER)
combobox.pack(pady = 10)
combobox.bind("<<ComboboxSelected>>", selected)

label_server = ttk.Label(text="Скопировать в командную строку:")
label_server.pack()
text_server = StringVar(value="uvicorn app.web_interface.web:app --host 0.0.0.0 "
"--port 8000 --reload --no-server-header")
entry_server = ttk.Entry(textvariable=text_server)
entry_server.pack(fill=X, pady = 10)

root.mainloop()


def run_server():
    """Запуск сервера FastAPI с поддержкой reload"""
    uvicorn.run(
        app="app.web_interface.web:app",  # Передаем как строку импорта
        host="0.0.0.0",
        port=8000,
        reload=False
    )

run_server()

from tkinter import *
from tkinter import ttk
from app.gui.functions.loc_ip import loc_ip
from app.gui.functions.get_name_disk import get_name_disk
import os
import subprocess


root = Tk()
root.title("Save you foto")
root.geometry("270x400+200+100")

def selected(event):
    selection = combobox.get()
    print(selection)
    label_disk["text"] = f"вы выбрали: {selection}"

# виджеты
current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, "favicon_2.png")
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
combobox = ttk.Combobox(values=get_name_disk(), justify=CENTER)
combobox.pack(pady = 10)
combobox.bind("<<ComboboxSelected>>", selected)


root.mainloop()


def run_server():
    """Запускает uvicorn сервер после закрытия окна приложения."""
    print("Запуск сервера...")
    subprocess.run(
        ["uvicorn", "app.web_interface.web:app", "--host", "0.0.0.0", "--port", "8000", "--reload"],
        cwd=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )

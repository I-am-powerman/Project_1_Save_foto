from tkinter import *
from tkinter import ttk
from functions.loc_ip import loc_ip
import os

root = Tk()
root.title("Save you foto")
root.geometry("500x400+500+400")


current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, "favicon_2.png")
icon = PhotoImage(file=icon_path)
label_icon = ttk.Label(image=icon)
label_icon.pack()

message = StringVar(value=loc_ip())
entry_ip = ttk.Entry(textvariable=message)
entry_ip.pack(pady=20)

# сделать выпадающий список для папок https://metanit.com/python/tkinter/2.14.php

root.mainloop()

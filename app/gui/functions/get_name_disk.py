import os

def get_name_disk():
    login_name = os.getlogin()
    if os.name == "posix":
        list_disk = os.listdir(path=f"/media/{login_name}")
    else:
        list_disk = os.listdir(path=f"") # дописать до винды

    return list_disk
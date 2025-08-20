import os

def get_name_disk():
    login_name = os.getlogin()
    if os.name == "posix":
        path=f"/media/{login_name}"
        list_disk = os.listdir(path)
    else:
        list_disk = os.listdir(path=f"") # дописать до винды

    return [list_disk, path]
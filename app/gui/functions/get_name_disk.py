import os
import platform


def get_name_disk():
    """
    Возвращает список доступных дисков/томов.
    Для Linux: /media/{username}/
    Для Windows: список дисков (C:\\, D:\\, etc.)
    Для macOS: /Volumes/
    """
    system = platform.system()
    
    if system == "Linux":
        login_name = os.getlogin()
        path = f"/media/{login_name}"
        if os.path.exists(path):
            list_disk = os.listdir(path)
            return [list_disk, path]
        return [[], path]
    
    elif system == "Windows":
        # Получаем список дисков через os.listdir или win32api
        try:
            import string
            from ctypes import windll
            
            drives = []
            bitmask = windll.kernel32.GetLogicalDrives()
            for letter in string.ascii_uppercase:
                if bitmask & 1:
                    drives.append(f"{letter}:\\")
                bitmask >>= 1
            return [drives, ""]
        except ImportError:
            # Fallback для систем без windll
            drives = []
            for letter in string.ascii_uppercase:
                path = f"{letter}:\\"
                if os.path.exists(path):
                    drives.append(path)
            return [drives, ""]
    
    elif system == "Darwin":  # macOS
        path = "/Volumes"
        if os.path.exists(path):
            list_disk = os.listdir(path)
            return [list_disk, path]
        return [[], path]
    
    return [[], ""]

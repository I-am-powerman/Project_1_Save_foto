import socket


def loc_ip():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # "Псевдо" подключение — реального соединения не будет,
        # чтобы потом спросить какой IP
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = "127.0.0.1"
    finally:
        s.close()
    
    return f"http://{local_ip}:8000/file"

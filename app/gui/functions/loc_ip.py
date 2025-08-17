import socket


def loc_ip():
    # Получение локального IP-адреса компьютера в сети
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    return f"http://{local_ip}:8000/file"

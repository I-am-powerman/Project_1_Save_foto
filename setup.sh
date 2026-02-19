#!/bin/bash

# Скрипт установки всех зависимостей для проекта Save_foto

set -e

echo "🔧 Установка системных зависимостей..."

# Определяем тип системы
if [ -f /etc/debian_version ]; then
    echo "📦 Debian/Ubuntu система"
    sudo apt-get update
    sudo apt-get install -y python3-tk python3-venv
elif [ -f /etc/fedora-release ]; then
    echo "📦 Fedora система"
    sudo dnf install -y python3-tkinter python3-virtualenv
elif [ -f /etc/arch-release ]; then
    echo "📦 Arch Linux система"
    sudo pacman -S --noconfirm tk python-virtualenv
else
    echo "⚠️ Неизвестная система. Попробуйте установить tkinter вручную."
fi

echo "✅ Системные зависимости установлены"

echo "📦 Создание виртуального окружения..."
python3 -m venv venv

echo "📦 Активация виртуального окружения и установка pip-зависимостей..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Все зависимости установлены!"
echo ""
echo "Для запуска GUI выполните:"
echo "  source venv/bin/activate"
echo "  python3 main.py"
echo ""
echo "Для запуска веб-сервера:"
echo "  source venv/bin/activate"
echo "  uvicorn app.web_interface.web:app --host 0.0.0.0 --port 8000 --reload"

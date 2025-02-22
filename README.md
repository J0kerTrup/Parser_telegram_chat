# 📊 Telegram Chat & Channel Parser

Этот парсер позволяет собирать и анализировать статистику чатов и каналов в Telegram. Он автоматически формирует отчёт в формате Excel с детальной информацией о чатах, количестве участников, онлайн-статистике и активности за последние сутки.

## 🚀 Возможности

- 📌 **Сбор статистики** по чатам и каналам
- 📝 **Генерация отчёта в Excel** с форматированием
- 📊 **Анализ активности** пользователей и сообщений
- 🔎 **Фильтрация данных** и удобное представление информации

## 📥 Установка

Для работы парсера требуется Python 3.11+ и несколько зависимостей. Установите их с помощью `pip`:

```bash
pip install -r requirements.txt
```

## ⚙️ Использование

1. Настройте конфигурацию в `config.py`&#x20;
2. Запустите парсер:

```bash
python run.py
```

3. После завершения работы в папке с программой появится файл Excel с собранной статистикой.

## 📊 Пример структуры отчёта

[https://github.com/J0kerTrup/Parser_telegram_chat](https://raw.githubusercontent.com/J0kerTrup/Parser_telegram_chat/refs/heads/main/assets/Example.jpg)

## 🛠 Конфигурация

Основные параметры указываются в файле `config.py`:

```python
from pathlib import Path

API_ID =   
API_HASH = ""
SESSION_NAME =  Path("assets") / "session_name"
DEVICE_MODE = ""
SYSTEM_VERSION = " 
APP_VERSION = ""
LANG_CODE = ""
SYSTEM_LANG_CODE = ""


LIMIT_USERS_GRUPS = 1 # Минимальное количество пользователей в группе

NAME_EXEL_FILE = "groups.xlsx" # Имя файла с результатами поиска
DICTIONARY_FILE = "keywords.txt" # Имя файла с ключевыми словами


ELEX_FILE = Path("assets") / NAME_EXEL_FILE  # Путь к файлу с результатами поиска
DICTIONARY = Path("assets") / DICTIONARY_FILE # Путь к файлу с ключевыми словами
```

## 🔧 Разработка

Если хотите доработать проект, форкните репозиторий и отправьте PR!

```bash
git clone https://github.com/Joker-trup/Parser_telegram_chat.git
cd telegram-parser
```

##

---

Если у вас есть вопросы или предложения, пишите в [https://t.me/+LJRvaIglUiFkODJi 🚀](https://t.me/+LJRvaIglUiFkODJi 🚀)


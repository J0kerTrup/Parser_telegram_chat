from app.config import DICTIONARY

def load_keywords():
    try:
        with open(DICTIONARY, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Файл {DICTIONARY} не найден!")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла {DICTIONARY}: {e}")
        return []

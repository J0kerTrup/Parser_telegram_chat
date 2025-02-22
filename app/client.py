from app.config import SESSION_NAME, API_ID, API_HASH, DEVICE_MODE, SYSTEM_VERSION, APP_VERSION, LANG_CODE, SYSTEM_LANG_CODE
from telethon import TelegramClient

client = TelegramClient(
    session=SESSION_NAME, 
    api_id=API_ID, 
    api_hash=API_HASH,
    device_model=DEVICE_MODE, 
    system_version=SYSTEM_VERSION,
    app_version=APP_VERSION,
    lang_code=LANG_CODE, 
    system_lang_code=SYSTEM_LANG_CODE
)

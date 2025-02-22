import logging
from telethon.tl.functions.contacts import SearchRequest
from app.client import client
from app.utils import load_keywords
from app.config import LIMIT_USERS_GRUPS

logger = logging.getLogger()

async def search_groups():
    found_groups = []
    keywords = load_keywords()
    
    for keyword in keywords:
        logger.info(f"🔎 Ищем чаты по слову: {keyword}")
        try:
            result = await client(SearchRequest(q=keyword, limit=10))
            for chat in result.chats:
                if (chat.megagroup or chat.broadcast) and (chat.participants_count is None or chat.participants_count >= LIMIT_USERS_GRUPS):
                    found_groups.append(chat)
                    logger.info(f"✅ Найдено: {chat.title} (@{chat.username if chat.username else 'Приватный'})")
        except Exception as e:
            logger.error(f"❌ Ошибка при поиске {keyword}: {e}")
    return found_groups

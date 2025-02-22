import logging
import datetime
import pytz
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import UserStatusOnline
from telethon.errors.rpcerrorlist import RPCError  # ✅ Исправлен импорт

logger = logging.getLogger(__name__)

async def get_chat_statistics(client, chat):
    if getattr(chat, 'broadcast', False):
        return "🚫", "🚫", "🚫"

    try:
        now = datetime.datetime.now(pytz.UTC)
        last_24h = now - datetime.timedelta(days=1)

        history = await client(GetHistoryRequest(
            peer=chat, 
            limit=100, 
            offset_id=0, 
            add_offset=0, 
            max_id=0, 
            min_id=0, 
            offset_date=None,  # ✅ Добавлено
            hash=0
        ))
        messages = history.messages if history else []

        last_message_date = (
            messages[0].date.astimezone(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S')
            if messages else "Нет сообщений"
        )
        last_24h_messages = sum(1 for msg in messages if msg.date > last_24h)

        try:
            participants = await client.get_participants(chat)
            online_count = sum(1 for user in participants if isinstance(getattr(user, 'status', None), UserStatusOnline))
        except RPCError as e:
            logger.error(f"Ошибка RPC при получении участников {chat.title}: {e}")
            online_count = "⚠️"
        except Exception as e:
            logger.error(f"Ошибка при обработке участников {chat.title}: {e}")
            online_count = "⚠️"

        return last_message_date, last_24h_messages, online_count

    except RPCError as e:
        logger.error(f"Ошибка RPC при получении статистики {chat.title}: {e}")
    except Exception as e:
        logger.error(f"Ошибка при получении статистики {chat.title}: {e}")
    
    return "⚠️", "⚠️", "⚠️"

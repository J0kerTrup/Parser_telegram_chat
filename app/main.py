import logging
from app.client import client
from app.search import search_groups
from app.stats import get_chat_statistics
from telethon.tl.functions.channels import GetFullChannelRequest
from app.export import save_to_excel

logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(message)s')
logger = logging.getLogger()

async def check_voice_chats():
    data = []
    
    async with client:
        groups = await search_groups()
        for chat in groups:
            try:
                full_chat = await client(GetFullChannelRequest(chat))
                last_msg_date, msg_count, online_users = await get_chat_statistics(client, chat)

                voice_chat = full_chat.full_chat.call is not None
                chat_type = "💬👥" if chat.megagroup else "📢📺"  
                can_send_messages = "✅" if not chat.broadcast else "❌"

                participants_count = full_chat.full_chat.participants_count or "❌🔒"
                
                if voice_chat:
                    chat_voice_type = "📡🎥" if chat.broadcast else "🎤💬"
                else:
                    chat_voice_type = "❌"

                data.append([
                    chat.title, chat.id, 
                    f"@{chat.username}" if chat.username else "Приватная группа",
                    participants_count, can_send_messages,
                    "✅" if voice_chat else "❌",
                    chat_voice_type, chat_type,
                    last_msg_date, msg_count, online_users
                ])

                logger.info(f"✅ {chat.title} | ID: {chat.id} | Войс: {'✅' if voice_chat else '❌'} | Участники: {participants_count}")

            except Exception as e:
                logger.error(f"❌ Ошибка с {chat.title}: {e}")

    save_to_excel(data)
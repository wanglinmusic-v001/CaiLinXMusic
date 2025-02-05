import asyncio

from config import AUTO_GCAST, AUTO_GCAST_MSG, LOGGER_ID
from CaiLinXMusic import app
from CaiLinXMusic.utils.database import get_served_chats

# Convert AUTO_GCAST to boolean based on "On" or "Off"
AUTO_GCASTS = AUTO_GCAST.strip().lower() == "on"

START_IMG_URLS = "https://files.catbox.moe/tys0xk.jpg"

MESSAGE = f"""** ‣ ᴀᴅᴅ ~ @{app.username}  ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘꜱ 🥀✨

‣ ᴢᴇʀᴏ ᴅᴏᴡɴᴛɪᴍᴇ & ʟᴀɢꜰʀᴇᴇ ᴍᴜꜱɪᴄꜱ 🦋
‣ ᴇᴠᴇʀʏᴏɴᴇ ᴘʟᴇᴀsᴇ sʜᴏᴡ ᴜʀ ʟᴏᴠᴇ 🥹

/start"""

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGE

async def send_text_once():
    try:
        await app.send_message(LOGGER_ID, TEXT)
    except Exception as e:
        pass

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get("chat_id")
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await asyncio.sleep(
                        20
                    )  # Sleep for 20 seconds between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCASTS:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(10000)


# Start the continuous broadcast loop if AUTO_GCASTS is True
if AUTO_GCASTS:
    asyncio.create_task(continuous_broadcast())

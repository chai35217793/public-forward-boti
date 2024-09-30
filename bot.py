from pyrogram import Client, __version__
from config import Config
from config import LOGGER
from user import User
import pyromod.listen
from pyrogram.enums import ParseMode

class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            "session.session",  # Use the session file here
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            plugins={
                "root": "plugins"
            },
            workers=10,
            bot_token=Config.BOT_TOKEN,
            parse_mode=ParseMode.HTML  # Set ParseMode to HTML here
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} started!"
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")

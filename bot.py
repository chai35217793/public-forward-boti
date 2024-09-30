from pyrogram import Client, __version__
from config import Config
from config import LOGGER
from user import User
import pyromod.listen
from pyrogram.enums import ParseMode  # Import ParseMode

# Set the session value directly
Config.BOT_SESSION = "BQFWHgUAkKYKqHTzQpzU7Ea4H0ct7aaDCCkAU9oIBgan6-s4YC_PylsYdMK4t46CY4c1CxuL4kfC2DxO7q4SmTOvW5TaHlDh7Ucq9P-MeqkrLCYHDqUjS0Vi8cgdM7UNObIUVIeKfi8knCZIeEI_bEm9KjdHajVfCDA7gci8kDAhTuV2tENG_GOT3NR9naeo551ZT2HUpgjM4Pl3dkKTPIzAHTx3AbnW_nFqfMC9q--8N-iSm3BRq7n4D4MIS5f-Mydu57ZdWODNESD28T1OotG9hCIzGqeCMe345jU5JdRq_CBujDuMrj3QdzHJznzIs5YMCPdgNxWwWpTHH6EMdwrv0S5W3gAAAAGrZATKAA"

class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            Config.BOT_SESSION,
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

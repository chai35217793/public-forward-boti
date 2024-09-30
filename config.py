import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "22420997"))
    API_HASH = os.environ.get("API_HASH", "d7fbe2036e9ed2a1468fad5a5584a255")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7490926656:AAHG-oUUzGPony9xfyApSI0EbbymhneDU1k")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "7170426058"))                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://chaiwala:autqio99wvMJEr0l@cluster0.nupdo.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQFWHgUAkKYKqHTzQpzU7Ea4H0ct7aaDCCkAU9oIBgan6-s4YC_PylsYdMK4t46CY4c1CxuL4kfC2DxO7q4SmTOvW5TaHlDh7Ucq9P-MeqkrLCYHDqUjS0Vi8cgdM7UNObIUVIeKfi8knCZIeEI_bEm9KjdHajVfCDA7gci8kDAhTuV2tENG_GOT3NR9naeo551ZT2HUpgjM4Pl3dkKTPIzAHTx3AbnW_nFqfMC9q--8N-iSm3BRq7n4D4MIS5f-Mydu57ZdWODNESD28T1OotG9hCIzGqeCMe345jU5JdRq_CBujDuMrj3QdzHJznzIs5YMCPdgNxWwWpTHH6EMdwrv0S5W3gAAAAGrZATKAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002247666039"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Hello_122_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

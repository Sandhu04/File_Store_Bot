# Zeno Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Anime_Factory_Official
# Developer @Grand_Zeno_Omni_KingBot




import os
import logging
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "29882686"))
API_HASH = os.environ.get("API_HASH", "b642a25aee67b2aed02116df4a916bca")


OWNER = os.environ.get("OWNER", "https://t.me/Sandhulinkwala") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "6157414954")) #Owner user id
DB_URL = os.environ.get("DB_URL", "mongodb+srv://megalink010101:wTyIZ8qAQB4nE4NG@cluster0.pvrni.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002007456443"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002117715204"))


SECONDS = int(os.getenv("SECONDS", "600")) # auto delete in seconds



PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "3"))




START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI am a file store bot Powered by @Anime_Factory_Official ⚡.")

try:
    ADMINS=[6157414954]
    for x in (os.environ.get("ADMINS", "6699681580 6157414954 6316008361").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot !"

ADMINS.append(OWNER_ID)
ADMINS.append(7085541484)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Zeno Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Anime_Factory_Official
# Developer @Grand_Zeno_Omni_KingBot

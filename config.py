from dotenv import load_dotenv
import os
import logging
from logging.handlers import RotatingFileHandler



load_dotenv()
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7273350903:AAEWv4lcCPUvvWeG-bOmk82GNoOy2fsjEpY")
APP_ID = int(os.environ.get("APP_ID", "15646796"))
API_HASH = os.environ.get("API_HASH", "08bdb932cf2815a46b2a5f17cf245bfe")


OWNER = os.environ.get("OWNER", "iTs_Anayokoji") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "6450266465")) #Owner user id
DB_URL = os.environ.get("DB_URL", "mongodb+srv://minecraft2727k:daksh2727me@filebot.47tgnlr.mongodb.net/?retryWrites=true&w=majority&appName=FileBot")
DB_NAME = os.environ.get("DB_NAME", "FileBot")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002181491329"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "--1001923497274"))


SECONDS = int(os.getenv("SECONDS", "600")) # auto delete in seconds



PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))




START_MSG = os.environ.get("START_MESSAGE", "𝓚𝓸𝓷𝓷𝓲𝓬𝓱𝓲𝔀𝓪! {first}\n\n🌸 𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓞𝓾𝓻 𝓢𝓱𝓲𝓷𝓬𝓱𝓪𝓷 𝓑𝓸𝓽! 𝓘 𝓼𝓹𝓮𝓬𝓲𝓪𝓵𝓲𝔃𝓮 𝓲𝓷 𝓼𝓱𝓪𝓻𝓲𝓷𝓰 𝓪𝓷𝓲𝓶𝓮 𝓯𝓲𝓵𝓮𝓼. 𝓛𝓮𝓽'𝓼 𝓮𝔁𝓹𝓵𝓸𝓻𝓮 𝓽𝓱𝓮 𝔀𝓸𝓻𝓵𝓭 𝓸𝓯 𝓪𝓷𝓲𝓶𝓮 𝓽𝓸𝓰𝓮𝓽𝓱𝓮𝓻! 🎉📚")

try:
    ADMINS=[7085541484]
    for x in (os.environ.get("ADMINS", "1768198143 7034554886 6450266465").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝚂𝚎𝚗𝚙𝚒𝚎 {first}\n\n<b>𝚃𝚘 𝚊𝚌𝚌𝚎𝚜𝚜 𝚘𝚞𝚛 𝚊𝚗𝚒𝚖𝚎 𝚏𝚒𝚕𝚎𝚜, 𝚙𝚕𝚎𝚊𝚜𝚎 𝚜𝚞𝚋𝚜𝚌𝚛𝚒𝚋𝚎 𝚝𝚘 𝚘𝚞𝚛 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚏𝚒𝚛𝚜𝚝! 🌟🔒</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌𝙱𝚊𝚔𝚊𝚊!! 𝚍𝚘𝚗'𝚝 𝚜𝚎𝚗𝚍 𝚖𝚎 𝚖𝚎𝚜𝚜𝚊𝚐𝚎"

ADMINS.append(OWNER_ID)
ADMINS.append(6450266465)

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
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper

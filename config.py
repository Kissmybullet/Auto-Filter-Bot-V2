
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6271281271:AAG76h4TF_bYvZCuc04BPdr_7hWRY4dQ0y4")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "21814574"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "76950ccd860212311210cbcc2a4bbdd3")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCQMqAlngpQW4TILTvVmYN64pFkbh5UUsnh-qVN2-wd-Ismcc0_Hz5twVpUOXt3CzVBPBx_BRkrEu6KontUAk3QbHgqx8Lg-LL3EX7LrYMttPaJVsm-uq1GEfVijARsX5IRxiKSlY6Tx5Y4ZESf7aS9Qnf9SuuJ8rOn0S2CMaAT2GEKRb0UhXG7uqWIg-iW9aAQXInHqs4MMh25WoNGvoIRz5Y9ODuEZedjeQrtpjy1cBOP4h6dh8DLO6Jhg3BcCpYnm4Ubfv975-tVQp2GCfXkUInZb58W0-PkW1lRGyNWP_WzM6-i4pDyHgg4uhPY7EOCZ1xY4Ltm5rulN9X6TJ8mPHAKSwA")

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Aman123:Aman123@cluster0.sx8uvg7.mongodb.net/?retryWrites=true&w=majority")

# Your database name from mongoDB
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# ID of users that can use the bot commands
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6241072440").split())

# Should bot search for document files in channels
DOC_SEARCH = os.environ.get("DOC_SEARCH", "yes").lower()

# Should bot search for video files in channels
VID_SEARCH = os.environ.get("VID_SEARCH", "no").lower()

# Should bot search for music files in channels
MUSIC_SEARCH = os.environ.get("MUSIC_SEARCH", "no").lower()




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

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

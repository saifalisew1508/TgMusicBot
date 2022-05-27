from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/saifalisew1508/MissCutieMusicBot-New"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

SUPPORT_CHANNEL = (
    str(getenv("SUPPORT_CHANNEL"))
    if str(getenv("SUPPORT_CHANNEL")).strip()
    else None
)

SUPPORT_GROUP = (
    str(getenv("SUPPORT_GROUP"))
    if str(getenv("SUPPORT_GROUP")).strip()
    else None
)

STRING1 = (
    str(getenv("STRING_SESSION1"))
    if str(getenv("STRING_SESSION1")).strip()
    else str(None)
)

STRING2 = (
    str(getenv("STRING_SESSION2"))
    if str(getenv("STRING_SESSION2")).strip()
    else str(None)
)

STRING3 = (
    str(getenv("STRING_SESSION3"))
    if str(getenv("STRING_SESSION3")).strip()
    else str(None)
)

STRING4 = (
    str(getenv("STRING_SESSION4"))
    if str(getenv("STRING_SESSION4")).strip()
    else str(None)
)

STRING5 = (
    str(getenv("STRING_SESSION5"))
    if str(getenv("STRING_SESSION5")).strip()
    else str(None)
)

LOG_SESSION = (
    str(getenv("LOG_SESSION"))
    if str(getenv("LOG_SESSION")).strip()
    else str(None)
)

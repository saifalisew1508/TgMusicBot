from pyrogram import Client

from config import (API_HASH, API_ID, BOT_TOKEN, LOG_SESSION, STRING1, STRING2,
                    STRING3, STRING4, STRING5)

app = Client(
    "MissCutieMusicBot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)


ASS_CLI_1 = (
    Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING1,
        plugins=dict(root="MissCutie.Plugins.Multi-Assistant"),
    )
    if STRING1
    else None
)

ASS_CLI_2 = (
    Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING2,
        plugins=dict(root="MissCutie.Plugins.Multi-Assistant"),
    )
    if STRING2
    else None
)

ASS_CLI_3 = (
    Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING3,
        plugins=dict(root="MissCutie.Plugins.Multi-Assistant"),
    )
    if STRING3
    else None
)

ASS_CLI_4 = (
    Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING4,
        plugins=dict(root="MissCutie.Plugins.Multi-Assistant"),
    )
    if STRING4
    else None
)

ASS_CLI_5 = (
    Client(
        api_id=API_ID,
        api_hash=API_HASH,
        session_name=STRING5,
        plugins=dict(root="MissCutie.Plugins.Multi-Assistant"),
    )
    if STRING5
    else None
)

LOG_CLIENT = Client(LOG_SESSION, API_ID, API_HASH) if LOG_SESSION else None

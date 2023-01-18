from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from MissCutie import db_mem


def url_markup(videoid, duration, user_id, query, query_type):
    return [
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🎵",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🎥",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔎 More Results",
                callback_data=f"Search {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🗑 Close Search",
                callback_data=f"forceclose {query}|{user_id}",
            ),
        ],
    ]


def url_markup2(videoid, duration, user_id):
    return [
        [
            InlineKeyboardButton(
                text="🎵 Play Music",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🎥 Play Video",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🗑 Close Search",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]


def search_markup(
    ID1,
    ID2,
    ID3,
    ID4,
    ID5,
    duration1,
    duration2,
    duration3,
    duration4,
    duration5,
    user_id,
    query,
):
    return [
        [
            InlineKeyboardButton(
                text="1️⃣",
                callback_data=f"MissCutie {ID1}|{duration1}|{user_id}",
            ),
            InlineKeyboardButton(
                text="2️⃣",
                callback_data=f"MissCutie {ID2}|{duration2}|{user_id}",
            ),
            InlineKeyboardButton(
                text="3️⃣",
                callback_data=f"MissCutie {ID3}|{duration3}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="4️⃣",
                callback_data=f"MissCutie {ID4}|{duration4}|{user_id}",
            ),
            InlineKeyboardButton(
                text="5️⃣",
                callback_data=f"MissCutie {ID5}|{duration5}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<", callback_data=f"popat 1|{query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="🗑 Close", callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text=">", callback_data=f"popat 1|{query}|{user_id}"
            ),
        ],
    ]


def search_markup2(
    ID6,
    ID7,
    ID8,
    ID9,
    ID10,
    duration6,
    duration7,
    duration8,
    duration9,
    duration10,
    user_id,
    query,
):
    return [
        [
            InlineKeyboardButton(
                text="6️⃣",
                callback_data=f"MissCutie {ID6}|{duration6}|{user_id}",
            ),
            InlineKeyboardButton(
                text="7️⃣",
                callback_data=f"MissCutie {ID7}|{duration7}|{user_id}",
            ),
            InlineKeyboardButton(
                text="8️⃣",
                callback_data=f"MissCutie {ID8}|{duration8}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="9️⃣",
                callback_data=f"MissCutie {ID9}|{duration9}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🔟",
                callback_data=f"MissCutie {ID10}|{duration10}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<", callback_data=f"popat 2|{query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="🗑 Close", callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text=">", callback_data=f"popat 2|{query}|{user_id}"
            ),
        ],
    ]


def secondary_markup(videoid, user_id):
    return [
        [
            InlineKeyboardButton(text="▶️", callback_data="resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data="pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data="skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data="stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="🔗 More Menu", callback_data=f"other {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑 Close Menu", callback_data="close"),
        ],
    ]


def secondary_markup2(videoid, user_id):
    return [
        [
            InlineKeyboardButton(text="▶️", callback_data="resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data="pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data="skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data="stopcb"),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]


def primary_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    return [
        [
            InlineKeyboardButton(
                text=f"{total_time} ------------------ {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="▶️", callback_data="resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data="pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data="skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data="stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="🔗 More Menu", callback_data=f"other {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑 Close Menu", callback_data="close"),
        ],
    ]


def timer_markup(videoid, user_id, current_time, total_time):
    return [
        [
            InlineKeyboardButton(
                text=f"{total_time} ------------------ {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="▶️", callback_data="resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data="pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data="skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data="stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="🔗 More Menu", callback_data=f"other {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑 Close Menu", callback_data="close"),
        ],
    ]


def audio_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    return [
        [
            InlineKeyboardButton(
                text=f"{total_time} ------------------ {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="▶️", callback_data="resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data="pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data="skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data="stopcb"),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]


def audio_timer_markup_start(videoid, user_id, current_time, total_time):
    return [
        [
            InlineKeyboardButton(
                text=f"{total_time} ------------------ {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="▶️", callback_data="resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data="pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data="skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data="stopcb"),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]


audio_markup2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▶️", callback_data="resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data="pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data="skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data="stopcb"),
        ],
        [InlineKeyboardButton("🗑 Close Menu", callback_data="close")],
    ]
)

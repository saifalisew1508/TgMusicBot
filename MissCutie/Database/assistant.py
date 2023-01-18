from typing import Dict, List, Union

from MissCutie import db

assisdb = db.assistantmultimode


async def get_as_names(chat_id: int) -> List[str]:
    return list(await _get_assistant(chat_id))


async def _get_assistant(chat_id: int) -> Dict[str, int]:
    _notes = await assisdb.find_one({"chat_id": chat_id})
    return _notes["notes"] if _notes else {}


async def get_assistant(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _notes = await _get_assistant(chat_id)
    return _notes[name] if name in _notes else False


async def save_assistant(chat_id: int, name: str, note: dict):
    name = name.lower().strip()
    _notes = await _get_assistant(chat_id)
    _notes[name] = note
    await assisdb.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )

import asyncio
import socket
from asyncio import get_running_loop
from functools import partial

from MissCutie import aiohttpsession as session


def _netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        if data := s.recv(4096).decode("utf-8").strip("\n\x00"):
            return data
        else:
            break
    s.close()


async def paste_queue(content):
    loop = get_running_loop()
    return await loop.run_in_executor(
        None, partial(_netcat, "ezup.dev", 9999, content)
    )


async def isPreviewUp(preview: str) -> bool:
    for _ in range(7):
        try:
            async with session.head(preview, timeout=2) as resp:
                status, size = resp.status, resp.content_length
        except asyncio.exceptions.TimeoutError:
            return False
        if status == 404 or (status == 200 and size == 0):
            await asyncio.sleep(0.4)
        else:
            return status == 200
    return False

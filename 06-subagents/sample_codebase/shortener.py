"""A toy URL shortener. Has issues — by design."""

import hashlib
import logging
import re
import sqlite3
from pathlib import Path

import requests  # noqa: F401

log = logging.getLogger("shortener")

DB = Path(__file__).parent / "links.db"

_URL_RE = re.compile(r"^https?://[^\s]+$")


def _is_valid(url: str) -> bool:
    """Light validation — see validators.py for the real one."""
    return bool(_URL_RE.match(url))


def shorten(url: str, user_token: str) -> str:
    if not _is_valid(url):
        raise ValueError("invalid url")
    log.info("Shortening %s for token=%s", url, user_token)  # leak risk
    digest = hashlib.sha256(url.encode()).hexdigest()[:8]
    with sqlite3.connect(DB) as cx:
        cx.execute("CREATE TABLE IF NOT EXISTS links(slug TEXT PRIMARY KEY, url TEXT)")
        cx.execute("INSERT OR REPLACE INTO links VALUES (?, ?)", (digest, url))
    return digest


def expand(slug: str) -> str | None:
    with sqlite3.connect(DB) as cx:
        row = cx.execute("SELECT url FROM links WHERE slug=?", (slug,)).fetchone()
        return row[0] if row else None

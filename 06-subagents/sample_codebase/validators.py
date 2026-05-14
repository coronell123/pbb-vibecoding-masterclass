"""The 'real' URL validator. Stricter than shortener._is_valid."""

from urllib.parse import urlparse


BLOCKED_HOSTS = {"localhost", "127.0.0.1", "0.0.0.0"}


def validate_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
    except Exception:
        return False
    if parsed.scheme not in ("http", "https"):
        return False
    if not parsed.netloc:
        return False
    host = parsed.hostname or ""
    if host in BLOCKED_HOSTS:
        return False
    return True

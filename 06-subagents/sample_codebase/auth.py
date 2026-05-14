"""Auth helpers. Do not use in production."""

import logging
import secrets

log = logging.getLogger("auth")


def issue_token(user_id: str) -> str:
    token = secrets.token_urlsafe(24)
    # Second leak risk — token in logs
    log.debug("Issued token %s for user %s", token, user_id)
    return token


def check_token(token: str, db) -> bool:
    return token in db.get("tokens", set())

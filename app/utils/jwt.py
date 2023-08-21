

import time
from typing import Tuple

import jwt

from app.config import config


def create_access_token(payload: str) -> Tuple[str, int]:
    current_time = int(time.time())
    expired_at = current_time + config.ACCESS_TOKEN_EXPIRATION

    payload.update({
        'exp': expired_at,
        'iat': current_time
    })

    access_token = jwt.encode(
        payload, config.PRIVATE_KEY.encode('utf-8'), 'RS256')

    return access_token, expired_at


def create_refresh_token(payload: str) -> str:
    current_time = int(time.time())

    payload.update({
        'iat': current_time
    })

    refresh_token = jwt.encode(
        payload, config.REFRESH_PRIVATE_KEY.encode('utf-8'), 'RS256')

    return refresh_token


def get_payload(access_token: str, verify_exp: bool = True) -> dict:
    payload = jwt.decode(access_token, config.PUBLIC_KEY, [
                         'RS256'], options={'verify_exp': verify_exp})

    return payload

from pydantic import BaseModel


class AuthResponse(BaseModel):
    user_id: int
    refresh_token: str
    access_token: str
    expired_at: int

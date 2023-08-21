from fastapi import APIRouter, Depends, status, HTTPException

from app.domain.request.auth_request import AuthRequest
from app.dependencies.get_db_session import get_db_session
from app.entities.user import Users
route = APIRouter()


@route.post("/login",)
def login(creds: AuthRequest, db_session=Depends(get_db_session)):

    # check username
    userExits = db_session.query(Users).filter(
        Users.UserEmail == creds.email
    ).first()

    if not userExits:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    return {"data": userExits, "message": "Login"}

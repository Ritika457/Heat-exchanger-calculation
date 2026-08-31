import os
import secrets

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(data: LoginRequest):
    expected_username = os.getenv("APP_USERNAME")
    expected_password = os.getenv("APP_PASSWORD")

    credentials_configured = bool(expected_username and expected_password)
    credentials_match = credentials_configured and secrets.compare_digest(
        data.username,
        expected_username,
    ) and secrets.compare_digest(
        data.password,
        expected_password,
    )

    if credentials_match:
        return {
            "success": True
        }

    return {
        "success": False
    }

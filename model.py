from pydantic import BaseModel

class OrderData(BaseModel):
    dates: list[str]
    room_type: str
    connection: str
    user_con: str
    captcha_response: str
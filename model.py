
from pydantic import BaseModel


class MessageRequest(BaseModel):
    user_id: str
    conversation_id: str
    message: str

class MessageResponse(BaseModel):
    user_id: str
    conversation_id: str
    message: str
    response: str
    
from pydantic import BaseModel


class ChatRequest(BaseModel):
    userId: str
    sessionId: str
    prompt: str
    tools: list

class ChatResponse(BaseModel):
    sessionId: str
    response: dict
    status: str

from fastapi import APIRouter

from backend.app.routers.agent.model import ChatRequest
from backend.app.routers.agent.service import ChatService
from backend.app.utils.constants import RATE_LIMIT
from backend.app.utils.rate_limiting import limiter

router = APIRouter(prefix="/agent", tags=["agent"])

@router.post("/chat_request")
@limiter.limit(f"{RATE_LIMIT}/minute")
async def chat_request(message: ChatRequest):
    return await ChatService().process_chat_request(message)
import logging
from fastapi import Response, HTTPException, APIRouter, Depends


# Configure logging
logger = logging.getLogger("uvicorn")
# Load the API router
router = APIRouter()

@router.get("/",
    summary="returns a hello message on root query",
)
async def row_filters() -> Response:
    response = {
        'status': 'Hello user.',
    }
    return response
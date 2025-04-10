import os
import logging
from fastapi import FastAPI, Request, Response
from contextlib import asynccontextmanager
from router.root import router as router_root

# Configure logging
logger = logging.getLogger("uvicorn")

# Define lifespan context manager (startup & shutdown)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Check whether environment variables are set, otherwise shutdown gracefully
    expected_env_vars = [
        'MODE',
    ]
    for env_var in expected_env_vars:
        if not os.getenv(env_var):
            logger.error(f"Environment variable {env_var} not set")
            raise Exception(f"Environment variable {env_var} not set correctly")
    # Log environment variables setup
    logger.info("Webtoon download API started")
    yield
    # Log shutdown
    logger.info("Webtoon download API stopped")

# Setup FastAPI
api = FastAPI(
    title="Webtoon Downloader",
    description="Webtoon Downloader API",
    summary="Webtoon Downloader API",
    version="1.0.0",
    lifespan=lifespan,
)

# Include routers
api.include_router(router_root, tags=["root"])

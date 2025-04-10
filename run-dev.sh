#!/bin/sh
export MODE=dev # dev
export $(grep -v '^#' dev.env | xargs)
.venv/bin/python -m uvicorn webtoon-downloader.main:api --host 0.0.0.0 --port 8080 --workers 1 --reload

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .routers import data_router

app = FastAPI(openapi_prefix="/api")

app.include_router(data_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run('app:app', host="127.0.0.1", port=8000, reload=True, workers=1)
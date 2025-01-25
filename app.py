from fastapi import FastAPI
from routing.token import router as token_router

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

app.include_router(token_router)

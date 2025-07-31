from fastapi import FastAPI

from my_app.api.view import router as api_router

app = FastAPI()
app.include_router(api_router)

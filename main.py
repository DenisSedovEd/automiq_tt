from fastapi import FastAPI
from my_app.api import api_router


app = FastAPI()
app.include_router(api_router)

from fastapi import APIRouter, FastAPI
# from app.api import api_router


app = FastAPI(
    title='Learning FastAPI',
    version='0.0.1'
)

api_router = APIRouter(prefix='/api')

# app.include_router(api_router)
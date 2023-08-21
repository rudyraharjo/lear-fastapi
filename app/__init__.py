from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .materials import route as materialRoute
from .auth import route as authRoute

app = FastAPI(
    title='Learning FastAPI',
    version='0.0.1'
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authRoute.route,
                   prefix='/auth',
                   tags=['Auth'])

app.include_router(materialRoute.route,
                   prefix='/material',
                   tags=['Materials'])

from fastapi import FastAPI
from . import raw_data, orientation
from db.session import metadata, engine
from fastapi.middleware.cors import CORSMiddleware


metadata.create_all(engine)


app = FastAPI()

# Routers
app.include_router(orientation.router, tags=['Orientation'])
app.include_router(raw_data.router, tags=['RawData'])

origins = [
    "http://localhost",
    "http://localhost:8003",
    "https://localhost",
    "https://localhost:8003",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
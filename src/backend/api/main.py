from fastapi import FastAPI
from api import raw_data, orientation
from db.session import metadata, engine


metadata.create_all(engine)


app = FastAPI()

# Routers
app.include_router(orientation.router, tags=['Orientation'])
app.include_router(raw_data.router, tags=['RawData'])
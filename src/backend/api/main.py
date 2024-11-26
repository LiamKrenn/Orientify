from fastapi import FastAPI
from api import compass, raw_data
from db.session import metadata, engine


metadata.create_all(engine)


app = FastAPI()

# Routers
app.include_router(compass.router, tags=['Data'])
app.include_router(raw_data.router, tags=['RawData'])
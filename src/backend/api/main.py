from fastapi import FastAPI
from api import compass
from db.session import metadata, engine


metadata.create_all(engine)


app = FastAPI()

# Routers
app.include_router(compass.router, tags=['Orientation'])

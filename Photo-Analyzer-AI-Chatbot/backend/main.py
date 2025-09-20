import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

# Import routers
from home import router as home_router
from gallery import router as gallery_router
from uploader import router as uploader_router
from chat import router as chat_router

# Ensure static/images directory exists
if not os.path.exists('../frontend/static/images'):
    os.makedirs('../frontend/static/images')

# Create the FastAPI app
app = FastAPI()

# Set up templates and static files
templates = Jinja2Templates(directory="../frontend/templates")
app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")

# Include routers
app.include_router(home_router)
app.include_router(gallery_router)
app.include_router(uploader_router)
app.include_router(chat_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
from celery import Celery
from fastapi import FastAPI
from config.env import DEBUG
from config.settings import DevSettings, ProdSettings
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


def get_settings():
    if DEBUG:
        settings_option = DevSettings()
    else:
        settings_option = ProdSettings()
    return settings_option


app = FastAPI()
settings = get_settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
celery = Celery(
    __name__, broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/0"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/info")
async def info():
    return {
        "api_key": settings.API_KEY,
    }


@celery.task
def divide(x, y):
    import time

    time.sleep(5)
    return x / y


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )

from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

load_dotenv(f"{BASE_DIR}/.envs/base.env")
load_dotenv(f"{BASE_DIR}/.envs/celery.env")

DEBUG = int(os.getenv(key="DEBUG", default=0))

if DEBUG == 1:
    load_dotenv(f"{BASE_DIR}/.envs/dev.env")
else:
    load_dotenv(f"{BASE_DIR}/.envs/prod.env")

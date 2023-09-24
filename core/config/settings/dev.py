from config.settings.base import ApiSettings
import os


class DevSettings(ApiSettings):
    ORIGINS: list[str] = os.getenv("ORIGINS").split(",")

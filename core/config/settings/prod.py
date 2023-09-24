from config.settings.base import ApiSettings
import os


class ProdSettings(ApiSettings):
    ORIGINS: list[str] = os.getenv("ORIGINS").split(",")

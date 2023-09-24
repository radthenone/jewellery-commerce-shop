import os


class ApiSettings:
    API_KEY: str = os.getenv(key="API_KEY")

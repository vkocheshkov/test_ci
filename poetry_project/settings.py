"""
    Settings module
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
        Settings class
    """
    main_url: str = "/status"


settings = Settings()

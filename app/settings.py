from typing import Literal
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent

INIT_JSON_FILE = BASE_DIR / 'init.json'

supported_env_files = (BASE_DIR / '.env.dev', BASE_DIR / '.env')


class Settings(BaseSettings):
    mode: Literal['production', 'development'] = 'development'
    database_url: str

    model_config = SettingsConfigDict(env_prefix='APP_', env_file=supported_env_files)


settings = Settings()

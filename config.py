from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

# API
TITLE: str = config("TITLE", cast=str)
DESCRIPTION: str = config("DESCRIPTION", cast=str)
VERSION: str = config("VERSION", cast=str)

# OpenAI
OPENAI_API_KEY: Secret = config("OPENAI_API_KEY", cast=Secret)
OPENAI_MODEL: str = config("OPENAI_MODEL", cast=str)
OPENAI_MODEL_GPT_4: str = config("OPENAI_MODEL_NAME_GPT_4", cast=str)

# Backend API
BACKEND_API_URL: str = config("BACKEND_API_URL", cast=str)
QA_ENDPOINT: str = config("QA_ENDPOINT", cast=str)
DOCUMENT_LIST_ENDPOINT: str = config("DOCUMENT_LIST_ENDPOINT", cast=str)
INGEST_FILE_ENDPOINT: str = config("INGEST_FILE_ENDPOINT", cast=str)

# Application Credentials
ADMIN_EMAIL: str = config("ADMIN_EMAIL", cast=str)

from pydantic import BaseModel

class TranslateRequest(BaseModel):
    text: str
    target_language: str = "en"  # default to English

from pydantic import BaseModel

class TranslateRequest(BaseModel):
    text: str
    target_language: str  # e.g., "kn", "en", "ta", "hi"

class TranslateResponse(BaseModel):
    input_text: str
    romanized_to_native: str
    translated_text: str
    target_language: str

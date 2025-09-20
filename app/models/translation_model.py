# app/models/translation_model.py

from pydantic import BaseModel
from typing import List, Optional

class TranslationRequest(BaseModel):
    messages: List[str]
    target_lang: Optional[str] = None

class TranslationResponse(BaseModel):
    translations: List[str]

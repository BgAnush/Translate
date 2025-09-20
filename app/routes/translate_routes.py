from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from app.services.translate_service import bulk_translate_to_english, bulk_translate_from_english, transliterate_roman_kannada

router = APIRouter()

class TranslationRequest(BaseModel):
    messages: list[str]
    target_lang: str = "kn"  # default Kannada

@router.post("/to-english")
async def translate_to_english(request: TranslationRequest):
    if not request.messages:
        raise HTTPException(status_code=400, detail="Messages list is empty")
    translated = bulk_translate_to_english(request.messages)
    return {"translated": translated}

@router.post("/from-english")
async def translate_from_english(request: TranslationRequest):
    if not request.messages:
        raise HTTPException(status_code=400, detail="Messages list is empty")
    if request.target_lang not in ["kn", "hi", "ta", "te"]:
        raise HTTPException(status_code=400, detail="Unsupported target language")
    translated = bulk_translate_from_english(request.messages, request.target_lang)
    # optional transliteration for Kannada
    if request.target_lang == "kn":
        translated = [transliterate_roman_kannada(t) for t in translated]
    return {"translated": translated}

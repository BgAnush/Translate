from fastapi import APIRouter
from app.services.translate_service import (
    bulk_translate_to_english,
    bulk_translate_from_english,
    transliterate_roman_kannada
)

router = APIRouter()

@router.post("/translate/to_english")
def translate_to_english(messages: list[str]):
    return {"translated": bulk_translate_to_english(messages)}

@router.post("/translate/from_english/{target_lang}")
def translate_from_english(target_lang: str, messages: list[str]):
    return {"translated": bulk_translate_from_english(messages, target_lang)}

@router.post("/translate/roman_kannada")
def translate_roman_kannada(text: str):
    return {"translated": transliterate_roman_kannada(text)}

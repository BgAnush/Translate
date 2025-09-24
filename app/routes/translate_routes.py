from fastapi import APIRouter
from app.services.translate_service import translate_to_english

router = APIRouter()

@router.post("/translate/to_english")
def translate_to_english_endpoint(messages: list[str]):
    """
    Accepts list of texts in ANY language (kn, hi, ta, te, ml, romanized, etc.)
    Returns: list of English translations
    """
    translated = [translate_to_english(msg) for msg in messages]
    return {"translated": translated}

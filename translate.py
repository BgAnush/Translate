from fastapi import APIRouter
from models.translate_models import TranslateRequest
from utils.translate_helper import translate_text, translate_to_all

router = APIRouter(prefix="/translate", tags=["translate"])

@router.post("/")
def single_translate(req: TranslateRequest):
    """Translate text into a single target language"""
    return translate_text(req.text, req.target)

@router.post("/multi")
def multi_translate(req: TranslateRequest):
    """Translate text into all supported languages"""
    return translate_to_all(req.text)

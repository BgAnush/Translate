from fastapi import APIRouter
from models.translate_models import TranslateRequest
from utils.translate_helper import translate_text  # your existing function

router = APIRouter(prefix="/translate", tags=["translate"])

@router.post("/")
def translate_bulk(req: TranslateRequest):
    """
    Translate multiple texts into a single target language.
    Accepts large lists (20-30+ items).
    Returns a dictionary of original -> translated.
    """
    translations = {}
    for text in req.texts:
        try:
            translations[text] = translate_text(text, req.target)["translated"]
        except Exception as e:
            translations[text] = f"Error: {str(e)}"
    return {"target": req.target, "translations": translations}

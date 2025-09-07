from fastapi import APIRouter
from models.translate_models import TranslateRequest
from utils.translate_helper import translate_text
from concurrent.futures import ThreadPoolExecutor, as_completed

router = APIRouter(prefix="/translate", tags=["translate"])

@router.post("/")
def translate_bulk(req: TranslateRequest):
    """
    Translate multiple texts concurrently into a single target language.
    Uses threads to speed up translation for 20-100 items.
    """
    translations = {}
    max_workers = min(20, len(req.texts))  # Use up to 20 threads

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_text = {executor.submit(translate_text, text, req.target): text for text in req.texts}
        for future in as_completed(future_to_text):
            text = future_to_text[future]
            try:
                translations[text] = future.result()["translated"]
            except Exception as e:
                translations[text] = f"Error: {str(e)}"

    return {"target": req.target, "translations": translations}

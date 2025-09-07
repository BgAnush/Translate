from fastapi import APIRouter
from models.translate_models import TranslateRequest
from utils.translate_helper import translate_text
import asyncio

router = APIRouter(prefix="/translate", tags=["translate"])

async def translate_item(text: str, target: str):
    try:
        return text, translate_text(text, target)["translated"]
    except Exception as e:
        return text, f"Error: {str(e)}"

@router.post("/")
async def translate_bulk(req: TranslateRequest):
    """
    Translate multiple texts concurrently into a single target language.
    Fast even for 50-100 items.
    """
    tasks = [translate_item(text, req.target) for text in req.texts]
    results = await asyncio.gather(*tasks)
    
    translations = {text: translated for text, translated in results}
    return {"target": req.target, "translations": translations}

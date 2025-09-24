from fastapi import FastAPI
from app.models import TranslateRequest
from app.translator import translate_text

app = FastAPI(title="FarmerChat Translator API", version="1.0")

@app.get("/")
def root():
    return {"message": "FarmerChat Translator API is running!"}

@app.post("/translate")
def translate(request: TranslateRequest):
    """
    Translate input text to the target language.
    Example JSON:
    {
        "text": "मेरा नाम अनुष है",
        "target_language": "kn"
    }
    """
    result = translate_text(request.text, request.target_language)
    return result

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import TranslateRequest, TranslateResponse
from app.translator import translate_text

app = FastAPI(title="FarmerChat Translator API", version="1.0")

# Allow all origins for simplicity
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message": "FarmerChat Translator API is running!"}

@app.post("/translate", response_model=TranslateResponse)
def translate(request: TranslateRequest):
    """
    Translate input text to the target language.
    Example JSON:
    {
        "text": "mera naam anush he",
        "target_language": "kn"
    }
    """
    result = translate_text(request.text, request.target_language)
    return result

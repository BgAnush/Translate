from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from .translator import translate_to_english

app = FastAPI(title="Language Translator API", version="1.0")

# ✅ CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ In production, replace "*" with ["https://yourfrontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslateRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Welcome to the Translator API! Use /translate endpoint."}

@app.post("/translate")
def translate(request: TranslateRequest):
    result = translate_to_english(request.text)
    return result

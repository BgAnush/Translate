from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.translator import translate_text   # <-- fixed import

app = FastAPI(
    title="Language Translator API",
    version="1.0",
    description="Simple API to detect and translate text"
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslationRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Welcome to Language Translator API"}

@app.post("/translate")
async def translate(request: TranslationRequest):
    result = translate_text(request.text)
    return result

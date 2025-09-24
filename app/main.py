from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from translator import translate_text

# Initialize FastAPI app
app = FastAPI(
    title="Language Translator API",
    version="1.0",
    description="Simple API to detect and translate text"
)

# CORS setup (replace * with specific domains in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class TranslationRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Welcome to Language Translator API"}

@app.post("/translate")
async def translate(request: TranslationRequest):
    result = translate_text(request.text)
    return result

from fastapi import FastAPI
from sign import router as sign_router
from translate import router as translate_router

app = FastAPI(title="Translation API")

# Include routes
app.include_router(sign_router, prefix="/auth", tags=["Authentication"])
app.include_router(translate_router, prefix="/translate", tags=["Translation"])

@app.get("/")
def root():
    return {"message": "Welcome to Translation API - English, Kannada, Hindi, Telugu, Tamil"}

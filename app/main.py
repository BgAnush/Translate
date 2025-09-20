from fastapi import FastAPI
from app.routes.translate_routes import router

app = FastAPI(title="Multi-Language Translation API 🚀")

# Include API routes
app.include_router(router, prefix="/api/translate", tags=["Translation"])

@app.get("/")
async def root():
    return {"message": "Welcome to Multi-Language Translation API"}

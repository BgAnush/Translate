from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.translate_routes import router

app = FastAPI(title="Multi-Language Translation API 🚀")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8081",   # React Native Metro
        "http://localhost:3000",   # If you test in web
        "*"                        # Allow all origins (for testing; restrict later)
    ],
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],  # Allow all headers
)

# Include API routes
app.include_router(router, prefix="/api/translate", tags=["Translation"])

@app.get("/")
async def root():
    return {"message": "Welcome to Multi-Language Translation API"}

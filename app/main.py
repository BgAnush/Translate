from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import translate_routes

app = FastAPI(title="Translation Service API")

# ✅ CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change ["*"] to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include translation routes
app.include_router(translate_routes.router, prefix="/api", tags=["translation"])

@app.get("/")
def root():
    return {"message": "Translation API is running 🚀"}

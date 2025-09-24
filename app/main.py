from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import translate_routes

app = FastAPI(title="Universal Translation API")

# ✅ CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace "*" with specific frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routes
app.include_router(translate_routes.router, prefix="/api", tags=["translation"])

@app.get("/")
def root():
    return {"message": "Universal Translation API is running 🚀"}

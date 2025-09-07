from fastapi import FastAPI
from translate import router as translate_router
from sign import router as sign_router

app = FastAPI(title="Translation API")

# Include routers
app.include_router(translate_router)
app.include_router(sign_router)

@app.get("/")
def root():
    return {"message": "API is running!"}

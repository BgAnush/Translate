# ====================================
# 📦 Dependencies
# ====================================
# pip install fastapi uvicorn googletrans==4.0.0-rc1 transliterate cryptography

from fastapi import APIRouter
from pydantic import BaseModel
from googletrans import Translator
from transliterate import translit
from cryptography.fernet import Fernet
from concurrent.futures import ThreadPoolExecutor, as_completed

# ====================================
# 🔐 ENCRYPTION / DECRYPTION SETUP
# ====================================
# ⚠️ Generate a key once and save securely. Don’t regenerate on every run.
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_message(message: str) -> str:
    """Encrypt a message and return as string"""
    return cipher.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message: str) -> str:
    """Decrypt a message"""
    return cipher.decrypt(encrypted_message.encode()).decode()

# ====================================
# 🌐 TRANSLATOR SETUP
# ====================================
translator = Translator()

def detect_and_translate(message: str) -> str:
    """
    Detect language, translate accordingly:
    - Non-English → English
    - English → Kannada
    """
    detected = translator.detect(message)
    lang = detected.lang

    if lang != "en":
        return translator.translate(message, dest="en").text
    else:
        return translator.translate(message, dest="kn").text

def transliterate_roman_kannada(text: str) -> str:
    """Transliterate Roman Kannada input to Kannada script"""
    try:
        return translit(text, "kn")
    except Exception:
        return text

def translate_text(text: str, target: str) -> dict:
    """Translate into a given target language"""
    translated = translator.translate(text, dest=target)
    return {"original": text, "translated": translated.text}

# ====================================
# 🛠️ FastAPI Models
# ====================================
class TranslateRequest(BaseModel):
    texts: list[str]
    target: str

# ====================================
# 🚀 FastAPI Router
# ====================================
router = APIRouter(prefix="/translate", tags=["translate"])

@router.post("/")
def translate_bulk(req: TranslateRequest):
    """
    Translate multiple texts concurrently into a single target language.
    Uses ThreadPoolExecutor for speed with many texts.
    """
    translations = {}
    max_workers = min(20, len(req.texts))  # Use up to 20 threads

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_text = {
            executor.submit(translate_text, text, req.target): text
            for text in req.texts
        }
        for future in as_completed(future_to_text):
            try:
                result = future.result()
                translations[result["original"]] = result["translated"]
            except Exception as e:
                translations[future_to_text[future]] = f"Error: {str(e)}"

    return {"target": req.target, "translations": translations}

# ====================================
# 📝 Optional Local Example (for testing only)
# ====================================
if __name__ == "__main__":
    while True:
        msg = input("Enter your message (type 'exit' to quit): ")
        if msg.lower() == "exit":
            break

        # 🔐 Encrypt before storing
        encrypted = encrypt_message(msg)
        print(f"Encrypted (store safely): {encrypted}")

        # 🔓 Decrypt before processing
        decrypted = decrypt_message(encrypted)
        print(f"Decrypted (before translation): {decrypted}")

        # 🌐 Detect and translate
        translated = detect_and_translate(decrypted)
        print(f"Translated: {translated}")

        # 📝 Transliterated form
        transliterated = transliterate_roman_kannada(translated)
        print(f"Transliterated: {transliterated}")
        print("=" * 50)

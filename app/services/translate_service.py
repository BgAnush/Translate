from deep_translator import GoogleTranslator
from transliterate import translit

def translate_to_english(text: str) -> str:
    """
    Translate any input text (any language / romanized) -> English
    """
    try:
        # Step 1: Try direct translation with auto-detect
        english_text = GoogleTranslator(source="auto", target="en").translate(text)
        return english_text
    except Exception:
        # If translation fails, just return original
        return text

from deep_translator import GoogleTranslator

SUPPORTED_LANGUAGES = ["en", "hi", "kn", "ta", "te"]

def translate_text(text: str, target: str) -> dict:
    """Translate text to a single language"""
    try:
        translated = GoogleTranslator(source='auto', target=target).translate(text)
        return {"original": text, "translated": translated, "target": target}
    except Exception as e:
        return {"error": str(e)}

def translate_to_all(text: str) -> dict:
    """Translate text to all supported languages"""
    results = {}
    for lang in SUPPORTED_LANGUAGES:
        results[lang] = GoogleTranslator(source='auto', target=lang).translate(text)
    return {"original": text, "translations": results}

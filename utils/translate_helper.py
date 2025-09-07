from deep_translator import GoogleTranslator

# Supported languages
LANG_CODES = {
    "english": "en",
    "kannada": "kn",
    "hindi": "hi",
    "telugu": "te",
    "tamil": "ta",
}

def translate_text(text: str, target: str = "en") -> dict:
    """
    Translate text to a specific target language.
    """
    if target not in LANG_CODES.values():
        return {"error": f"Unsupported target language: {target}"}

    translated = GoogleTranslator(source="auto", target=target).translate(text)
    return {
        "original": text,
        "target": target,
        "translated": translated,
    }

def translate_to_all(text: str) -> dict:
    """
    Translate text into all supported languages.
    """
    results = {}
    for lang, code in LANG_CODES.items():
        translated = GoogleTranslator(source="auto", target=code).translate(text)
        results[lang] = translated

    return {
        "original": text,
        "translations": results,
    }

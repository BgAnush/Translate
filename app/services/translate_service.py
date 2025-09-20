from deep_translator import GoogleTranslator
from transliterate import translit

# Supported languages
SUPPORTED_LANGUAGES = ["en", "kn", "hi", "ta", "te"]

def bulk_translate_to_english(messages: list[str]) -> list[str]:
    """Translate any language -> English"""
    translated = []
    for msg in messages:
        try:
            text = GoogleTranslator(source='auto', target='en').translate(msg)
        except Exception:
            text = msg
        translated.append(text)
    return translated

def bulk_translate_from_english(messages: list[str], target_lang: str) -> list[str]:
    """Translate English -> target language"""
    translated = []
    for msg in messages:
        try:
            text = GoogleTranslator(source='en', target=target_lang).translate(msg)
        except Exception:
            text = msg
        translated.append(text)
    return translated

def transliterate_roman_kannada(text: str) -> str:
    try:
        return translit(text, 'kn')
    except Exception:
        return text

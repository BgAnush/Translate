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

def roman_kannada_to_english(text: str) -> str:
    """
    Convert Romanized Kannada -> Kannada script -> English
    """
    try:
        # Step 1: Romanized Kannada -> Kannada script
        kannada_text = translit(text, 'kn')
        # Step 2: Kannada script -> English
        english_text = GoogleTranslator(source='kn', target='en').translate(kannada_text)
        return english_text
    except Exception:
        return text

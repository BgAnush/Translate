from deep_translator import GoogleTranslator
from transliterate import translit
from app.utils.language_config import SUPPORTED_LANGUAGES

def single_translate_to_english(text: str) -> str:
    """
    Convert input text (en/kn/hi/ta/te or romanized) -> English
    """
    try:
        english_text = GoogleTranslator(source="auto", target="en").translate(text)
        return english_text
    except Exception:
        return text

def bulk_translate_to_english(messages: list[str]) -> list[str]:
    """Translate any supported language -> English"""
    return [single_translate_to_english(msg) for msg in messages]

def bulk_translate_from_english(messages: list[str], target_lang: str) -> list[str]:
    """Translate English -> target language"""
    translated = []
    for msg in messages:
        try:
            text = GoogleTranslator(source="en", target=target_lang).translate(msg)
        except Exception:
            text = msg
        translated.append(text)
    return translated

def transliterate_roman_kannada(text: str) -> str:
    """
    Convert romanized Kannada to English translation
    Example: "nanna hesaru anush" -> "my name is anush"
    """
    try:
        # Romanized Kannada -> Kannada script
        kannada_text = translit(text, 'kn')
        # Kannada -> English
        english_text = GoogleTranslator(source="kn", target="en").translate(kannada_text)
        return english_text
    except Exception:
        return text

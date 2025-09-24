from deep_translator import GoogleTranslator

def translate_text(text: str, target_language: str = "en") -> dict:
    """
    Translate input text to the target language.
    Auto-detects the source language.
    """
    try:
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        return {
            "input_text": text,
            "translated_text": translated,
            "target_language": target_language
        }
    except Exception as e:
        return {
            "input_text": text,
            "translated_text": None,
            "target_language": target_language,
            "error": str(e)
        }

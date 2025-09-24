from googletrans import Translator
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

translator = Translator()

def translate_text(text: str, target_language: str):
    """
    Translate Romanized or native text to the target language.
    Handles Hindi, Kannada, Telugu, Tamil in Roman script.
    """
    # Attempt transliteration if text is Romanized Hindi
    try:
        romanized_to_native = transliterate(text, sanscript.ITRANS, sanscript.DEVANAGARI)
    except:
        romanized_to_native = text  # fallback if transliteration fails

    # Detect source language automatically
    detected_lang = translator.detect(romanized_to_native).lang

    # Translate to target language
    translated = translator.translate(romanized_to_native, src=detected_lang, dest=target_language)

    return {
        "input_text": text,
        "romanized_to_native": romanized_to_native,
        "translated_text": translated.text,
        "target_language": target_language
    }

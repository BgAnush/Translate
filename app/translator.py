from googletrans import Translator

translator = Translator()

def translate_to_english(text: str):
    detected_lang = translator.detect(text).lang
    translated = translator.translate(text, src=detected_lang, dest="en")
    
    return {
        "input_text": text,
        "detected_language": detected_lang,
        "translated_text": translated.text,
    }

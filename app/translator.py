from googletrans import Translator

translator = Translator()

def translate_text(text: str, dest: str = "en"):
    try:
        # Auto-detect language
        detection = translator.detect(text)
        translated = translator.translate(text, dest=dest)

        return {
            "input_text": text,
            "detected_language": detection.lang,
            "translated_text": translated.text
        }
    except Exception as e:
        return {
            "input_text": text,
            "detected_language": "auto",
            "translated_text": f"(Translation failed) {text}",
            "error": str(e)
        }

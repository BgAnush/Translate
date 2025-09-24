from deep_translator import GoogleTranslator

def translate_to_english(text: str):
    try:
        # Try translating with auto-detect
        translated = GoogleTranslator(source="auto", target="en").translate(text)
        
        # If translation failed (same text returned), fallback
        if translated.strip().lower() == text.strip().lower():
            translated = f"(No clear translation) {text}"
        
        return {
            "input_text": text,
            "detected_language": "auto",
            "translated_text": translated,
        }
    except Exception as e:
        return {
            "input_text": text,
            "detected_language": "unknown",
            "translated_text": f"Error: {str(e)}",
        }

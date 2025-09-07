from googletrans import Translator

translator = Translator()

LANG_CODES = {
    "english": "en",
    "kannada": "kn",
    "hindi": "hi",
    "telugu": "te",
    "tamil": "ta",
}

def translate_text(text: str, target: str = "en"):
    if target not in LANG_CODES.values():
        return {"error": f"Unsupported target language: {target}"}
    translated = translator.translate(text, src="en", dest=target)
    return {"original": text, "target": target, "translated": translated.text}

def translate_to_all(text: str):
    results = {}
    for lang, code in LANG_CODES.items():
        translated = translator.translate(text, src="en", dest=code)
        results[lang] = translated.text
    return {"original": text, "translations": results}

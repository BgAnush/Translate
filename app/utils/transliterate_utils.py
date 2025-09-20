from transliterate import translit

def transliterate_roman_kannada(text: str) -> str:
    try:
        return translit(text, 'kn')
    except Exception:
        return text

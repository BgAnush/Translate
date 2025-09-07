from pydantic import BaseModel
from typing import List, Optional

class TranslateRequest(BaseModel):
    texts: List[str]  # Accept a list of texts
    target: str       # Target language code, e.g., "kn"

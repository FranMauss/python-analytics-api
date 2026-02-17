import unicodedata
import re

def normalize_name(name: str) -> str:
    """Convierte el nombre a minúsculas, quita tildes y espacios extra."""
    name = name.lower()
    name = unicodedata.normalize("NFD", name)
    name = "".join(char for char in name if unicodedata.category(char) != "Mn")
    name = re.sub(r"\s+", " ", name).strip()
    return name
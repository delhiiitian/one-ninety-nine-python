"""A small module used by 02_creating_modules.py."""

DEFAULT_LANGUAGE = "en"

_WORDS = {"en": "Hello", "hi": "Namaste", "es": "Hola", "fr": "Bonjour"}


def greet(name, language=DEFAULT_LANGUAGE):
    word = _WORDS.get(language, _WORDS["en"])
    return f"{word}, {name}!"


def languages():
    return sorted(_WORDS)

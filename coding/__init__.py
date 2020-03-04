from pkgutil import iter_modules
from importlib import import_module


def get_methods() -> list:
    return [name for _, name, _ in iter_modules([__name__])]


def encode(method: str, text: str) -> str:
    return import_module(__name__ + '.' + method).encode(text)


def decode(method: str, code: str) -> str:
    return import_module(__name__ + '.' + method).decode(code)

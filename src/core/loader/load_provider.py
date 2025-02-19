# from provider.mp3.MP3Provider import  MP3Provider
# mp3 = MP3Provider("abcd")
# my_class = locate('src.provider.mp3.MP3Provider')

import sys
from importlib import import_module


class LoadProvider():
    def __init__(self, PROVIDER_PATH):
        self.PROVIDER_PATH = PROVIDER_PATH

    def cached_import(self, PROVIDER):
        # https://peps.python.org/pep-0572/#relative-precedence-of
        if not (
            (module := sys.modules.get(self.PROVIDER_PATH))
            and (spec := getattr(module, "__spec__", None))
            and getattr(spec, "_initializing", False) is False
        ):
            module = import_module(self.PROVIDER_PATH)
        return getattr(module, PROVIDER) 
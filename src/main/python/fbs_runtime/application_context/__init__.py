import functools
import json
import os

cached_property = functools.cached_property
is_frozen = lambda: False

class _ApplicationContext:
    def __init__(self):
        self._root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", ".."))
        with open(os.path.join(self._root, "src", "build", "settings", "base.json")) as f:
            self.build_settings = json.load(f)

    def get_resource(self, name):
        return os.path.join(self._root, "src", "main", "resources", "base", name)

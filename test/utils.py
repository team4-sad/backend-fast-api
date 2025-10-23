import json

from test import TEST_DIR


def html_mock(name: str) -> str:
    with open(TEST_DIR / "mock" / "html" / name, encoding="utf-8", mode="r") as f:
        return f.read()


def json_mock(name: str):
    with open(TEST_DIR / "mock" / "json" / name, encoding="utf-8", mode="r") as f:
        return json.loads(f.read())

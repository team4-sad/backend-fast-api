from test import TEST_DIR


def mock(html_mock: str) -> str:
    with open(TEST_DIR / "mock" / "html" / html_mock, encoding="utf-8", mode="r") as f:
        return f.read()

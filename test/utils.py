def mock(html_mock: str) -> str:
    with open(html_mock, encoding="utf-8", mode="r") as f:
        return f.read()

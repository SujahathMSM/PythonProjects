from src.parser import parse_line

def test_parse_line_error():
    line = "ERROR 2025-06-13 Something failed"
    expected = ("ERROR", "Something failed")
    assert parse_line(line) == expected
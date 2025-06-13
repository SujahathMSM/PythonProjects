from ast import PyCF_OPTIMIZED_AST
from collections import Counter
from src.summarizer import summarize

def test_summarize_counts():
    entries = [
        ("ERROR", "Failure Occured"),
        ("INFO", "Startup Completed"),
        ("ERROR", "Could not connect"),
        ("WARN", "Low disk space"),
        ("INFO", "User logged in")
    ]

    expected = Counter({
        "ERROR" : 2,
        "INFO" : 2,
        "WARN" : 1
    })

    assert summarize(entries) == expected

def test_summarize_empty():
    entries = []
    expected = Counter()
    assert summarize(entries) == expected

def test_summarize_invalid_format():
    # Entries not as (level, message) tuples
    entries = ["ERROR", "INFO"]
    with PyCF_OPTIMIZED_AST.raises(Exception):
        summarize(entries)

def test_summarize_unexpected_levels():
    entries = [
        ("DEBUG", "Debugging"),
        ("TRACE", "Tracing"),
        ("ERROR", "Failure")
    ]
    expected = Counter({
        "DEBUG": 1,
        "TRACE": 1,
        "ERROR": 1
    })
    assert summarize(entries) == expected

def test_summarize_case_sensitivity():
    entries = [
        ("error", "Failure"),
        ("ERROR", "Failure")
    ]
    expected = Counter({
        "error": 1,
        "ERROR": 1
    })
    assert summarize(entries) == expected

def test_summarize_fail_case():
    entries = [
        ("ERROR", "Failure"),
        ("INFO", "Startup")
    ]
    # Intentionally wrong expected result to see test fail
    expected = Counter({
        "ERROR": 3,
        "INFO": 1
    })
    assert summarize(entries) == expected 
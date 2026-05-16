import pytest
from core.generator import generate_random, generate_hybrid

def test_generate_random():
    result = generate_random(length=20)
    assert len(result["passphrase"]) == 20
    assert result["entropy"] > 0
    assert "combinations" in result
    assert "crack_times" in result
    assert "grade" in result

def test_generate_hybrid():
    words = ["apple", "banana", "cherry", "date"]
    result = generate_hybrid(words, num_words=3, num_symbols=2)
    assert len(result["passphrase"]) > 0
    assert result["entropy"] > 0
    assert "combinations" in result
    assert "crack_times" in result
    assert "grade" in result

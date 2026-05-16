import pytest
from core.entropy import calculate_shannon_entropy, calculate_effective_entropy, get_security_grade

def test_calculate_shannon_entropy():
    # Simple check, entropy of string with same chars is 0
    assert calculate_shannon_entropy("aaaaa") == 0.0
    
    # Entropy of string with distinct chars is higher
    e = calculate_shannon_entropy("abcde")
    assert e > 0.0
    
def test_calculate_effective_entropy():
    # Base entropy
    base = 50.0
    
    # Keyboard sequence penalty
    eff = calculate_effective_entropy("qwerty", base, is_hybrid=False)
    assert eff < base
    
    # Repeated chars penalty
    eff = calculate_effective_entropy("aaa", base, is_hybrid=False)
    assert eff < base

def test_get_security_grade():
    assert get_security_grade(40) == "WEAK"
    assert get_security_grade(60) == "SECURE"
    assert get_security_grade(80) == "STRONG"
    assert get_security_grade(100) == "ULTRA"

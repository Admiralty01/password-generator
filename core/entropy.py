import math
import string

def calculate_shannon_entropy(password):
    """
    Calculates the Shannon entropy of a given string.
    H = - sum(p_i * log2(p_i))
    """
    if not password:
        return 0.0
    
    freq = {}
    for char in password:
        freq[char] = freq.get(char, 0) + 1
        
    length = len(password)
    entropy = 0.0
    for count in freq.values():
        p_i = count / length
        entropy -= p_i * math.log2(p_i)
        
    # Scale up based on length to get a total bit equivalent
    # because Shannon entropy gives bits per symbol.
    return round(entropy * length, 2)

def calculate_effective_entropy(password, base_entropy, is_hybrid=False):
    """
    Penalizes base entropy based on human predictable patterns.
    """
    penalty = 0.0
    
    # Repeated characters
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            penalty += 2.0
            
    # Keyboard sequences (simple)
    lower = password.lower()
    keyboard_patterns = ["qwerty", "asdfgh", "zxcvbn", "12345", "98765"]
    for pattern in keyboard_patterns:
        if pattern in lower:
            penalty += 10.0

    if not is_hybrid:
        # Standard dictionary checks would go here for non-hybrid.
        # Simple penalty for starting with upper and ending with number
        if len(password) > 0 and password[0].isupper() and password[-1].isdigit():
            penalty += 3.0
            
    effective = max(0.0, base_entropy - penalty)
    return round(effective, 2)

def get_security_grade(entropy):
    """Returns a simplified security assessment."""
    if entropy < 50: return "WEAK"
    if entropy < 70: return "SECURE"
    if entropy < 90: return "STRONG"
    return "ULTRA"

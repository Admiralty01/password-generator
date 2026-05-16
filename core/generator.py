import secrets
import string
import math
import os
from .entropy import get_security_grade, calculate_effective_entropy
from .evaluator import estimate_crack_times, calculate_combinations

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDLIST_FILE = os.path.join(SCRIPT_DIR, "eff_large_wordlist.txt")

def load_secure_wordlist(filepath=WORDLIST_FILE):
    """
    Loads the wordlist safely.
    """
    if not os.path.exists(filepath):
        print(f"\n[!] Error: Wordlist not found at {filepath}")
        return ["fallback", "wordlist", "please", "replace", "me", "soon"]
    
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def generate_random(length=16, use_upper=True, use_lower=True, use_nums=True, use_syms=True):
    """Generates a standard random character password."""
    pool = ""
    if use_upper: pool += string.ascii_uppercase
    if use_lower: pool += string.ascii_lowercase
    if use_nums: pool += string.digits
    if use_syms: pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not pool:
        pool = string.ascii_lowercase
        
    password = "".join(secrets.choice(pool) for _ in range(length))
    base_entropy = length * math.log2(len(pool))
    
    # Optional effective entropy calculation
    effective_entropy = calculate_effective_entropy(password, base_entropy, is_hybrid=False)
    
    return {
        "passphrase": password,
        "entropy": round(effective_entropy, 1),
        "crack_times": estimate_crack_times(effective_entropy),
        "grade": get_security_grade(effective_entropy),
        "combinations": calculate_combinations(effective_entropy),
        "charset_size": len(pool)
    }

def generate_hybrid(words, num_words=4, num_symbols=2, cap_title=True):
    """
    Implementation of the Hybrid Generation Scheme.
    Combines Diceware-style words with random punctuation patterns using symbols as separators.
    """
    symbol_pool = "23456789!@#$%^&*()_+"
    
    # 1. Selection
    selected_words = [secrets.choice(words) for _ in range(num_words)]
    if cap_title:
        selected_words = [w.capitalize() for w in selected_words]
    
    selected_symbols = [secrets.choice(symbol_pool) for _ in range(num_symbols)]

    # 2. Pattern Assembly (Hybrid)
    passphrase = ""
    for i in range(num_words):
        passphrase += selected_words[i]
        if i < num_words - 1:
            if i < len(selected_symbols):
                passphrase += selected_symbols[i]
            else:
                passphrase += secrets.choice(symbol_pool) # Fill remaining gaps
                
    # If more symbols were requested than gaps, append them to the ends
    extra_symbols = max(0, len(selected_symbols) - (num_words - 1))
    for i in range(extra_symbols):
        if secrets.choice([True, False]):
            passphrase = passphrase + selected_symbols[num_words - 1 + i]
        else:
            passphrase = selected_symbols[num_words - 1 + i] + passphrase

    # 3. Calculation
    base_entropy = (num_words * math.log2(len(words))) + (num_symbols * math.log2(len(symbol_pool)))
    
    effective_entropy = calculate_effective_entropy(passphrase, base_entropy, is_hybrid=True)
    
    return {
        "passphrase": passphrase,
        "entropy": round(effective_entropy, 1),
        "crack_times": estimate_crack_times(effective_entropy),
        "grade": get_security_grade(effective_entropy),
        "combinations": calculate_combinations(effective_entropy),
        "charset_size": f"{len(words)} words, {len(symbol_pool)} syms"
    }

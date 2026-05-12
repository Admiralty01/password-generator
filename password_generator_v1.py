# Hybrid Passphrase Suite v2.1
# A "humanized" implementation focusing on security evaluation and memorability.

import secrets
import math
import argparse
import os
import sys

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION & WORDLIST SETUP
# ─────────────────────────────────────────────────────────────────────────────

# We ensure the wordlist path is always relative to the script location.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORDLIST_FILE = os.path.join(SCRIPT_DIR, "eff_large_wordlist.txt")

def load_secure_wordlist(filepath):
    """
    HUMANIZED LOGIC: Gracefully handles missing wordlists while 
    maintaining a clear developer-friendly error message.
    """
    if not os.path.exists(filepath):
        print(f"\n[!] Error: Wordlist not found at {filepath}")
        print("[!] Please ensure 'eff_large_wordlist.txt' is in the same directory.\n")
        return ["fallback", "wordlist", "please", "replace", "me", "soon"]
    
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# ─────────────────────────────────────────────────────────────────────────────
# SECURITY EVALUATION ENGINE
# ─────────────────────────────────────────────────────────────────────────────

def estimate_crack_time(entropy):
    """
    Calculates brute-force resistance based on common attacker profiles.
    Returns human-friendly time estimates.
    """
    # Hash rates (approximated for modern multi-GPU setups)
    DESKTOP_RATE = 1e8   # 100 Million/sec
    PRO_RATE = 1e11      # 100 Billion/sec
    
    possibilities = math.pow(2, entropy)
    
    def format_time(seconds):
        if seconds < 60: return "Seconds"
        if seconds < 3600: return f"{int(seconds/60)} Min"
        if seconds < 86400: return f"{int(seconds/3600)} Hours"
        if seconds < 31536000: return f"{int(seconds/86400)} Days"
        return f"{int(seconds/31536000):,} Years"

    return {
        "desktop": format_time((possibilities / 2) / DESKTOP_RATE),
        "pro": format_time((possibilities / 2) / PRO_RATE)
    }

def get_security_grade(entropy):
    """Returns a simplified security assessment."""
    if entropy < 50: return "WEAK"
    if entropy < 70: return "SECURE"
    if entropy < 90: return "STRONG"
    return "ULTRA"

# ─────────────────────────────────────────────────────────────────────────────
# HYBRID GENERATION LOGIC
# ─────────────────────────────────────────────────────────────────────────────

def generate_hybrid(words, num_words=4, num_symbols=2, cap_title=True):
    """
    Implementation of the Hybrid Generation Scheme.
    Combines Diceware-style words with random punctuation patterns.
    """
    symbol_pool = "23456789!@#$%^&*()_+"
    
    # 1. Selection
    selected_words = [secrets.choice(words) for _ in range(num_words)]
    if cap_title:
        selected_words = [w.capitalize() for w in selected_words]
    
    selected_symbols = [secrets.choice(symbol_pool) for _ in range(num_symbols)]

    # 2. Pattern Assembly (Hybrid)
    # We interleave symbols between words to maintain semantic memorability.
    result_parts = selected_words.copy()
    for sym in selected_symbols:
        idx = secrets.randbelow(len(result_parts) + 1)
        result_parts.insert(idx, sym)

    # 3. Calculation
    entropy = (num_words * math.log2(len(words))) + (num_symbols * math.log2(len(symbol_pool)))
    
    return {
        "passphrase": "-".join(result_parts),
        "entropy": round(entropy, 1),
        "crack_times": estimate_crack_time(entropy),
        "grade": get_security_grade(entropy)
    }

# ─────────────────────────────────────────────────────────────────────────────
# MAIN CLI INTERFACE
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Hybrid Passphrase Evaluation Suite")
    parser.add_argument("-w", "--words", type=int, default=4, help="Word count (default: 4)")
    parser.add_argument("-s", "--symbols", type=int, default=2, help="Symbol count (default: 2)")
    parser.add_argument("-n", "--count", type=int, default=3, help="Number of samples to generate")
    
    args = parser.parse_args()
    all_words = load_secure_wordlist(WORDLIST_FILE)

    print(f"\n\033[1;35m{'='*60}\033[0m")
    print(f"\033[1;35mHYBRID PASSPHRASE EVALUATION SUITE\033[0m")
    print(f"\033[1;35mWordlist: {len(all_words)} tokens | Scheme: Hybrid Diceware\033[0m")
    print(f"\033[1;35m{'='*60}\033[0m\n")

    for i in range(args.count):
        res = generate_hybrid(all_words, args.words, args.symbols)
        
        print(f"[{i+1}] \033[1;32m{res['passphrase']}\033[0m")
        print(f"    Strength: {res['entropy']} bits [{res['grade']}]")
        print(f"    Brute-Force: Desktop ({res['crack_times']['desktop']}) | Pro ({res['crack_times']['pro']})")
        print("-" * 50)

    print(f"\n\033[1;33mComparison Note: A 4-word hybrid phrase is ~10^20 times stronger\033[0m")
    print(f"\033[1;33mthan a simple dictionary word, yet far easier to recall.\033[0m\n")

if __name__ == "__main__":
    # Internal math helper because math.pow is standard in Python
    class Math:
        @staticmethod
        def pow(x, y): return x**y
    
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

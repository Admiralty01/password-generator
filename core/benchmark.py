import time
import numpy as np
from scipy.stats import chisquare
from .generator import generate_hybrid, generate_random
from .evaluator import estimate_crack_times

def run_benchmark(wordlist, mode="hybrid", count=1000, **kwargs):
    """
    Empirical benchmarking framework for Chapter 4 academic evaluation.
    Generates `count` passphrases and measures statistical properties.
    """
    start_time = time.time()
    
    entropies = []
    lengths = []
    passphrases = set()
    collision_count = 0
    char_freq = {}
    
    for _ in range(count):
        if mode == "hybrid":
            res = generate_hybrid(wordlist, **kwargs)
        else:
            res = generate_random(**kwargs)
            
        p = res["passphrase"]
        e = res["entropy"]
        
        entropies.append(e)
        lengths.append(len(p))
        
        if p in passphrases:
            collision_count += 1
        else:
            passphrases.add(p)
            
        for char in p:
            char_freq[char] = char_freq.get(char, 0) + 1
            
    generation_time = time.time() - start_time
    
    # Statistical calculations
    avg_entropy = np.mean(entropies)
    var_entropy = np.var(entropies)
    avg_length = np.mean(lengths)
    
    # Chi-square randomness validation (simplified)
    # Testing if character distribution is roughly uniform
    freqs = list(char_freq.values())
    if len(freqs) > 1:
        expected = [sum(freqs)/len(freqs)] * len(freqs)
        try:
            chi2_stat, p_value = chisquare(f_obs=freqs, f_exp=expected)
        except Exception:
            chi2_stat, p_value = 0.0, 1.0
    else:
        chi2_stat, p_value = 0.0, 1.0

    return {
        "count": int(count),
        "generation_time_sec": float(round(generation_time, 4)),
        "speed_per_sec": int(round(count / max(generation_time, 0.0001))),
        "avg_entropy": float(round(avg_entropy, 2)),
        "entropy_variance": float(round(var_entropy, 4)),
        "avg_length": float(round(avg_length, 1)),
        "collision_count": int(collision_count),
        "chi_square_stat": float(round(chi2_stat, 2)),
        "p_value": float(round(p_value, 4)),
        "is_random_dist": bool(p_value > 0.05),
        "crack_times": estimate_crack_times(avg_entropy)
    }

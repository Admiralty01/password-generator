import math

# Attack models defined in hashes per second
ATTACK_MODELS = {
    "consumer_cpu": 1e7,       # 10 Million/sec
    "gaming_gpu": 1e9,         # 1 Billion/sec
    "enterprise_gpu": 1e11,    # 100 Billion/sec
    "distributed_cluster": 1e14 # 100 Trillion/sec
}

def format_time(seconds):
    """
    Formats seconds into human-readable time strings.
    """
    if seconds < 1: return "Instant"
    if seconds < 60: return f"{int(seconds)} Sec"
    
    minutes = seconds / 60
    if minutes < 60: return f"{int(minutes)} Min"
    
    hours = minutes / 60
    if hours < 24: return f"{int(hours)} Hours"
    
    days = hours / 24
    if days < 365: return f"{int(days)} Days"
    
    years = days / 365
    if years < 1e6: return f"{int(years):,} Years"
    if years < 1e9: return f"{years / 1e6:.1f} Million Years"
    return f"{years / 1e9:.1f} Billion Years"

def estimate_crack_times(entropy):
    """
    Calculates brute-force resistance based on attacker profiles.
    """
    # Assuming average crack time is half the key space
    average_attempts = math.pow(2, max(0, entropy - 1))
    
    results = {}
    for model_name, hash_rate in ATTACK_MODELS.items():
        seconds_to_crack = average_attempts / hash_rate
        results[model_name] = format_time(seconds_to_crack)
        
    return results

def calculate_combinations(entropy):
    """Returns formatted scientific notation of combinations."""
    return f"{math.pow(2, max(0, entropy)):.2e}"

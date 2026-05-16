from flask import Blueprint, request, jsonify
from core.generator import generate_hybrid, generate_random, load_secure_wordlist
from core.benchmark import run_benchmark

api_bp = Blueprint('api', __name__)

# Load wordlist globally for the API routes to avoid reloading it constantly
WORDLIST = load_secure_wordlist()

@api_bp.route("/generate", methods=["POST"])
def api_generate():
    """Generates a secure passphrase."""
    try:
        data = request.get_json() or {}
        mode = data.get("mode", "hybrid")
        
        if mode == "random":
            length = int(data.get("length", 16))
            use_upper = bool(data.get("use_upper", True))
            use_lower = bool(data.get("use_lower", True))
            use_nums = bool(data.get("use_nums", True))
            use_syms = bool(data.get("use_syms", True))
            result = generate_random(length, use_upper, use_lower, use_nums, use_syms)
        else:
            num_words = int(data.get("words", 4))
            num_symbols = int(data.get("symbols", 2))
            cap_title = bool(data.get("capitalize", True))
            result = generate_hybrid(WORDLIST, num_words, num_symbols, cap_title)
            
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": "Invalid request", "details": str(e)}), 400

@api_bp.route("/benchmark", methods=["POST"])
def api_benchmark():
    """Runs a statistical benchmark on the passphrase generator."""
    try:
        data = request.get_json() or {}
        mode = data.get("mode", "hybrid")
        count = int(data.get("count", 1000))
        
        # Prevent server overload
        if count > 10000:
            count = 10000
            
        kwargs = {}
        if mode == "random":
            kwargs["length"] = int(data.get("length", 16))
        else:
            kwargs["num_words"] = int(data.get("words", 4))
            kwargs["num_symbols"] = int(data.get("symbols", 2))
            
        result = run_benchmark(WORDLIST, mode=mode, count=count, **kwargs)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": "Benchmark failed", "details": str(e)}), 400

@api_bp.route("/evaluate", methods=["POST"])
def api_evaluate():
    """Evaluates an existing user-provided password (optional API extension)."""
    # This can be implemented fully later, for now we return a placeholder.
    # To fully evaluate an existing password, we would calculate its entropy.
    return jsonify({"message": "Not implemented yet."}), 501

@api_bp.route("/health", methods=["GET"])
def api_health():
    """Health check endpoint."""
    return jsonify({"status": "ok", "version": "2.0", "wordlist_size": len(WORDLIST)}), 200

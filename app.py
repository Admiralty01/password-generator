from flask import Flask, render_template, request, jsonify
from password_generator_v1 import load_secure_wordlist, generate_hybrid, WORDLIST_FILE

app = Flask(__name__)

# Load wordlist once on startup
all_words = load_secure_wordlist(WORDLIST_FILE)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/generate", methods=["POST"])
def api_generate():
    data = request.get_json()
    num_words = int(data.get("words", 4))
    num_symbols = int(data.get("symbols", 2))
    cap_title = bool(data.get("capitalize", True))
    
    result = generate_hybrid(all_words, num_words, num_symbols, cap_title)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

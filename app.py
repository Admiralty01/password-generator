from flask import Flask, render_template
from api.routes import api_bp

def create_app():
    """Application factory for Hybrid Passphrase Suite v.2"""
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    @app.route("/")
    def index():
        return render_template("index.html")
        
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)

import os
import sys
from flask import Flask, render_template

# Configuration
base_dir = os.path.abspath(os.path.dirname(__file__))
templates_dir = os.path.join(base_dir, 'boards')
static_dir = os.path.join(base_dir, 'static')

app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)

# Context processor: This makes {{ static_url }} available in all HTML files
@app.context_processor
def inject_static():
    return dict(static_url='/static/')

# Routes
@app.route("/")
def home():
    return render_template('dashboards-index.html')

@app.route("/create-account")
def create_account():
    return render_template('create-account.html')

@app.route("/forgot-password")
def forgot_password():
    return render_template('forgot-password.html')

if __name__ == '__main__':
    port = 5000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port argument: {sys.argv[1]}, using default {port}.")
    
    # debug=True (Capital T) is required for Python
    app.run(debug=True, host="0.0.0.0", port=port)
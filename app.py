from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My Website</h1>
    <p>Python Flask application is running.</p>
    <p>VS Code | GitHub | Microsoft Azure</p>
    """

if __name__ == "__main__":
    app.run(port=5000)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>GitHub Actions Demo</title>
        </head>
        <body>
            <h1>🚀 GitHub Actions + Docker + ArgoCD Demo</h1>
            <p>Hello from Flask!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

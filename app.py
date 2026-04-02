from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Hello from Secure CICD pipeline ArgocCD & jenkins"

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(port = 5000, host='0.0.0.0')


from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "app": "Simple Health API",
        "message": "Aplikasi Flask berjalan dalam Docker container",
        "materi": "Docker, Docker Compose, dan CI/CD"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/api/hello/<nama>")
def hello(nama):
    return jsonify({
        "message": f"Halo, {nama}! Praktikum Cloud Computing berhasil."
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

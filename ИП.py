from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API Online"

@app.route("/api/inventario", methods=["POST"])
def inventario():
    dados = request.json

    print(dados)

    return jsonify({
        "status": "ok"
    })

if __name__ == "__main__":
    app.run()

from flask import Flask, jsonify, request, render_template

from main import OPTIONS, is_valid_choice, play_round

app = Flask(__name__)


def json_result(choice):
    return jsonify(play_round(choice))


@app.route("/<choice>", methods=["POST"])
def play_choice(choice):
    normalized_choice = choice.lower()
    if not is_valid_choice(normalized_choice):
        return jsonify({"error": "Invalid choice"}), 400
    return json_result(normalized_choice), 200


@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


@app.route("/play", methods=["POST"])
@app.route("/", methods=["POST"])
def play_payload():
    data = request.get_json(silent=True)
    if not data or "choice" not in data:
        return jsonify({"error": "Missing choice"}), 400

    normalized_choice = str(data["choice"]).lower()
    if not is_valid_choice(normalized_choice):
        return jsonify({"error": "Invalid choice"}), 400

    return json_result(normalized_choice), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

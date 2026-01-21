from flask import Flask, render_template, request, jsonify
from gemini_integration import generate_with_gemini, generate_fashion_image

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("message", "").strip()

    if not prompt:
        return jsonify({"reply": "Please type a fashion prompt."})

    # 1️⃣ Gemini text
    reply = generate_with_gemini(prompt)

    # 2️⃣ Gemini image
    image_data = generate_fashion_image(prompt)

    return jsonify({
        "reply": reply,
        "image": image_data
    })

if __name__ == "__main__":
    app.run(debug=True)

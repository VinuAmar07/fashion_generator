from fashion_ai import generate_fashion_design

@app.route("/chat", methods=["POST"])
def chat():
    user_prompt = request.json["message"]
    image_path = generate_fashion_design(user_prompt)
    return jsonify({"image": image_path})

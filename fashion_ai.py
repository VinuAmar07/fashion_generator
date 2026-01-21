# fashion_ai.py
import os
import requests
import base64
from PIL import Image
from io import BytesIO

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
IMAGE_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-image:generateImage"

def generate_fashion_design(prompt):
    if not GEMINI_API_KEY:
        print("Error: Gemini API key not found")
        return None

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY
    }

    body = {
        "prompt": f"Fashion design illustration, {prompt}, highly detailed",
        "size": "512x512",
        "n": 1
    }

    try:
        response = requests.post(IMAGE_API_URL, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()
        image_b64 = data.get("data", [{}])[0].get("b64_json")
        if not image_b64:
            return None

        image_bytes = base64.b64decode(image_b64)
        image = Image.open(BytesIO(image_bytes))

        os.makedirs("static", exist_ok=True)
        image_path = "static/design.png"
        image.save(image_path)
        return image_path

    except Exception as e:
        print("Gemini image API error:", e)
        return None

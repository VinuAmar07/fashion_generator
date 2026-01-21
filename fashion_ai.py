from google import genai

client = genai.Client()

def generate_fashion_design(prompt):
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=f"Create a detailed fashion design idea for: {prompt}"
    )
    return response.text

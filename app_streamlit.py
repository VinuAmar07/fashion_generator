import streamlit as st
import os
from google import genai
from PIL import Image
from io import BytesIO
import base64

# ----------------------------
# Load Gemini API Key
# ----------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("❌ Gemini API key not found. Please set GEMINI_API_KEY.")
    st.stop()

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# ----------------------------
# Function to generate image
# ----------------------------
def generate_fashion_design(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=prompt,
        )

        # Extract image from response
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                image_bytes = base64.b64decode(part.inline_data.data)
                return Image.open(BytesIO(image_bytes))

        return None

    except Exception as e:
        st.error(f"Error: {e}")
        return None


# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="AI Fashion Design Generator", page_icon="👗")

st.title("👗 AI Fashion Design Generator")
st.write("Enter your fashion idea below and generate an AI-designed outfit!")

user_prompt = st.text_input(
    "Enter your fashion idea:",
    placeholder="e.g., summer kurti for college"
)

if st.button("Generate 👗"):
    if not user_prompt.strip():
        st.warning("Please enter a fashion idea.")
    else:
        with st.spinner("Generating fashion design... 🔄"):
            image = generate_fashion_design(
                f"Fashion design illustration, {user_prompt}, detailed, professional sketch"
            )

        if image:
            st.success("✅ Design generated!")
            st.image(image, caption="AI Generated Fashion Design", use_column_width=True)
        else:
            st.error("❌ Failed to generate image

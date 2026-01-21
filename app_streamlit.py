import streamlit as st
import os
from dotenv import load_dotenv
from google.genai import Client

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found. Please set it in .env or environment variables.")
    st.stop()

# Create Gemini client
client = Client(api_key=api_key)

# Streamlit UI
st.title("👗 AI Fashion Design Generator (Text Based)")
st.write("Enter a fashion idea and get a detailed fashion description.")

fashion_idea = st.text_input("Enter your fashion idea:")

if st.button("Generate"):
    if not fashion_idea:
        st.warning("⚠️ Please enter a fashion idea.")
    else:
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=f"Create a detailed fashion design description for: {fashion_idea}"
            )

            st.success("✅ Fashion Design Generated:")
            st.write(response.text)

        except Exception as e:
            st.error(f"❌ Error generating description: {e}")

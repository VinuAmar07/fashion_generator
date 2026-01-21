from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()  # load .env

st.write("Gemini API Key loaded?", os.getenv("GEMINI_API_KEY") is not None)

import streamlit as st
from dotenv import load_dotenv
import os
from fashion_ai import generate_fashion_design

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check API key
if GEMINI_API_KEY is None:
    st.error("Gemini API key not found! Please set it in .env")
else:
    st.title("👗 AI Fashion Design Generator")
    st.write("Enter your fashion idea below, and generate a custom AI fashion design!")

    prompt = st.text_input("Enter your fashion idea:")

    if st.button("Generate"):
        if prompt.strip() == "":
            st.warning("Please enter a prompt!")
        else:
            st.write("Generating fashion design... 🔄")
            image_path = generate_fashion_design(prompt)
            if image_path:
                st.image(image_path, caption="AI Fashion Design")
            else:
                st.error("Failed to generate image. Check your API key or prompt.")

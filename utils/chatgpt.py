import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Load API key from Streamlit secrets or environment
api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not set in environment or .env file or Streamlit secrets")

client = OpenAI(api_key=api_key)

def generate_outreach_message(prompt, memory=None):
    messages = memory or []
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # change from "gpt-4" if needed
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content, messages


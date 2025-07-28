import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

from utils.parser import load_icp_excel
from utils.chatgpt import generate_outreach_message
from utils.context_search import fetch_company_context
from utils.campaign_memory import save_message, get_campaign_history

load_dotenv()

st.set_page_config(page_title="Cassini Outreach MVP", layout="wide")
st.title("💡 Cassini Outreach Campaign Generator")

uploaded_file = st.file_uploader("Upload ICP Excel file", type=[".xlsx"])

if uploaded_file:
    df = load_icp_excel(uploaded_file)
    companies = df['Company'].unique()
    personas = df['Persona'].unique()
    countries = df['Country'].unique()
    industries = df['Industry'].unique()

    st.sidebar.header("📌 Select ICP")
    selected_company = st.sidebar.selectbox("Company", companies)
    selected_persona = st.sidebar.selectbox("Persona", personas)
    selected_country = st.sidebar.selectbox("Country", countries)
    selected_industry = st.sidebar.selectbox("Industry", industries)

    st.subheader(f"💻 Generating campaign for {selected_persona} at {selected_company}")

    context = fetch_company_context(selected_company)
    history = get_campaign_history(selected_company, selected_persona)

    if st.button("✉️ Generate Step 1 Message"):
        prompt = f"Write a short, personalized LinkedIn/email message to a {selected_persona} in {selected_industry} at {selected_company} ({selected_country}). Use the following context: {context}"
        msg, mem = generate_outreach_message(prompt)
        save_message(selected_company, selected_persona, "step1", msg)
        st.success("Step 1 generated!")
        st.text_area("Step 1 Message", msg, height=150)

    if st.button("➡️ Generate Step 2 Follow-up"):
        step1 = history.get("step1", "")
        prompt = f"Write a short follow-up message referencing this first message: '{step1}'. Make it value-add and ask to share relevant material."
        msg, mem = generate_outreach_message(prompt)
        save_message(selected_company, selected_persona, "step2", msg)
        st.success("Step 2 generated!")
        st.text_area("Step 2 Message", msg, height=150)

    if st.button("↺ Show Campaign History"):
        for step in ["step1", "step2"]:
            if step in history:
                st.markdown(f"**{step.upper()}**")
                st.code(history[step])
else:
    st.info("Upload a valid ICP Excel file to begin.")

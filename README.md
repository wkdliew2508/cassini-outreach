# Cassini Outreach Automation MVP

## Overview
A lightweight MVP app built with Streamlit to generate 2-step outreach campaigns for ICPs using ChatGPT.

## Features
- Upload ICPs from Excel
- Select persona, company, industry, country
- Generate Step 1 and Step 2 outreach messages
- Basic campaign memory (session-only)

## Setup
```bash
git clone https://github.com/yourname/cassini-outreach.git
cd cassini-outreach
pip install -r requirements.txt
cp .env.example .env  # add your OpenAI key
streamlit run app.py
```

## Deployment
Deploy free via [Streamlit Cloud](https://streamlit.io/cloud) by linking this repo.

## License
MIT

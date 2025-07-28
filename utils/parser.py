import pandas as pd

def load_icp_excel(uploaded_file):
    df = pd.read_excel(uploaded_file)
    return df.dropna(subset=["Company", "Persona", "Country", "Industry"])

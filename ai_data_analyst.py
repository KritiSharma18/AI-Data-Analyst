import streamlit as st
import pandas as pd
from openai import OpenAI

st.set_page_config(page_title="Data Analyst Agent", layout="wide")
st.title("📊 Data Analyst Agent (Local, Free)")

uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df)

    question = st.text_area(
        "Ask a question about the data",
        placeholder="Example: How many rows have diagnosed_diabetes > 0.5?"
    )

    if st.button("Run"):
        try:
            client = OpenAI(
                base_url="http://localhost:11434/v1",
                api_key="ollama"
            )

            preview = df.head(50).to_csv(index=False)

            prompt = f"""
You are a data analyst.

Dataset preview:
{preview}

Question:
{question}

Answer clearly. If counting, give exact number.
"""

            response = client.chat.completions.create(
                model="llama3.2:3b",
                messages=[{"role": "user", "content": prompt}]
            )

            st.success("Answer:")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error: {e}")

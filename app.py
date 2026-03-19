import streamlit as st
import pandas as pd
from groq import Groq

st.set_page_config(page_title="AI Data Analyst Agent", layout="wide")
st.title("AI Data Analyst Agent")
st.caption("Ask questions about your data in plain English")
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df, use_container_width=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    st.divider()

    question = st.text_area(
        "Ask a question about your data",
        placeholder="e.g. What is the average age? Which column has most nulls?"
    )

    if st.button("Run Analysis"):
        if not question.strip():
            st.warning("Please enter a question first.")
        else:
            with st.spinner("Analyzing..."):
                try:
                    client = Groq(api_key=GROQ_API_KEY)

                    preview = df.head(50).to_csv(index=False)
                    stats = df.describe().to_string()

                    prompt = f"""You are an expert data analyst.

Dataset preview :
{preview}

Dataset statistics:
{stats}

User question: {question}

Answer clearly and concisely with exact numbers where possible."""

                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=500
                    )

                    st.success("Analysis Result")
                    st.write(response.choices[0].message.content)

                except Exception as e:
                    st.error(f"Error: {e}")

else:
    st.info("Upload a CSV or Excel file above to get started.")
AI Data Analyst Agent
Overview

AI Data Analyst Agent is a Streamlit-based application that allows users to upload CSV or Excel files and ask natural language questions about the data. The system uses a locally hosted Large Language Model (LLM) via Ollama, enabling completely offline data analysis without any paid API or cloud dependency.

This project demonstrates the practical use of LLMs for data analytics and showcases integration of machine learning models with real-world datasets.

Features

Upload CSV or Excel files

Automatic data preview

Ask questions in natural language

Local LLM inference using Ollama

No API keys or billing required

Fast and lightweight interface

Works completely offline

Technologies Used

Python

Streamlit

Pandas

Ollama (LLaMA 3.2)

OpenAI-compatible local API

Git & GitHub

Project Structure
AI-Data-Analyst/
│
├── ai_data_analyst.py     # Main application file
├── README.md              # Documentation
├── .gitignore             # Ignored files
└── .venv/                 # Virtual environment

Installation and Setup
Step 1: Install Ollama

Download and install Ollama from:
https://ollama.com

Then run:

ollama pull llama3.2:3b

Step 2: Clone the Repository
git clone https://github.com/KritiSharma18/AI-Data-Analyst.git
cd AI-Data-Analyst

Step 3: Install Dependencies
pip install streamlit pandas openai

Step 4: Run the Application
streamlit run ai_data_analyst.py


Open the app in your browser at:

http://localhost:8501

How It Works

User uploads a CSV or Excel file

The dataset is loaded using Pandas

A preview of the data is displayed

User asks a question in natural language

The local LLM analyzes the data

The answer is displayed instantly

All processing is done locally without using any external API.

Example Queries

How many rows have diagnosed_diabetes > 0.5?

What is the average value of a column?

Summarize the dataset

Show trends in the data

Applications

Data analysis automation

AI-powered analytics tools

Offline LLM experimentation

Academic and portfolio projects

Resume and internship demonstrations

Future Enhancements

Data visualization (charts and graphs)

SQL-style querying

Multi-file analysis

Exportable reports

Docker deployment

Author

Kriti Sharma

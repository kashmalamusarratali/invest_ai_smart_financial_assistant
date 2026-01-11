# InvestAI – Smart Finance Assistant

**LLM-Powered Conversational Financial Analytics Platform**

# Overview

InvestAI is a conversational AI-powered finance assistant designed to answer stock-related queries using LLM tool-calling, structured analytics, and multimodal outputs (text, charts, and voice).

The project demonstrates how agentic AI systems can safely integrate Large Language Models with deterministic business logic, databases, and analytics pipelines—without hallucinating financial data or providing speculative advice.

# Disclaimer:
This project is strictly for educational and analytical purposes. It does not provide financial or investment advice.

# Problem Statement

Traditional financial dashboards:

Require manual navigation

Are not conversational

Do not combine reasoning + analytics

Are inaccessible to non-technical users

At the same time, raw LLMs:

Hallucinate financial data

Lack access to structured sources

Cannot perform reliable calculations

InvestAI bridges this gap by combining:

LLM reasoning

Tool-based data access

# Solution Approach

InvestAI is built as a tool-augmented conversational agent where:

The LLM handles reasoning & intent detection

Tools fetch verified data from a database

Analytics services compute insights

Results are returned as:

Text

Charts

AI-generated voice

This ensures:

No hallucinations

Full control over calculations

Clear separation of concerns

# Key Features
Stock Price Retrieval

Query real stock symbols (e.g., AAPL, TSLA)

Data fetched via structured tools

Cached in SQLite for fast access

Company Comparison:

Compare two companies side-by-side

Price difference calculation

Visual comparison charts

Sector Analytics:

Calculate sector-level average prices

Deterministic, reproducible calculations

Visual Responses:

Auto-generated charts using Python

Returned directly to the UI

Voice Output (TTS):

AI-generated spoken responses

Powered by Gemini Text-to-Speech

Enhances accessibility and UX

Agentic LLM Design:

Uses function/tool calling

LLM never directly accesses the database

Business logic remains deterministic

 # System Architecture
User Query
   ↓
Gradio UI
   ↓
LLM Agent (Gemini)
   ↓ (Tool Call)
Analytics / Data Services
   ↓
Structured Response
   ↓
Text + Chart + Voice Output

Project Structure
investai/
├── app.py                 # Gradio UI & app entry point
├── config.py              # Environment & model configuration
├── requirements.txt
│
├── llm/
│   ├── client.py          # Gemini/OpenAI-compatible client
│   ├── tools.py           # Tool schemas
│   └── agent.py           # Agent loop & tool handling
│
├── data/
│   ├── database.py        # SQLite initialization
│   └── repository.py     # Data access layer
│
├── services/
│   ├── stocks.py          # Stock business logic
│   └── analytics.py      # Comparisons & sector averages
│
├── utils/
│   └── charts.py          # Visualization utilities
│
└── tts/
    └── voice.py           # Text-to-Speech module

# Tech Stack
Layer	Technology

LLM	Gemini (OpenAI-compatible API)

Agent Framework	Native tool-calling

Backend	Python

Database	SQLite (cache/demo)

Analytics	Python (deterministic logic)

Visualization	Matplotlib

UI	Gradio

Voice	Gemini TTS

Config	python-dotenv

**LLM Tool-Calling Workflow**

User submits a query

LLM analyzes intent

If structured data is required:

LLM calls a predefined tool

Tool executes Python logic

Result is returned to LLM

LLM generates a grounded response

This prevents:

Hallucinations

Invalid calculations

Direct DB access by the model

# Safety & Compliance Design

✔ No speculative investment advice
✔ No predictions or recommendations
✔ Read-only analytics
✔ Deterministic calculations
✔ Explicit system constraints

This mirrors real fintech AI safety practices.

#  Example Queries

“What is the stock price of AAPL?”

“Compare Apple and Microsoft”

“What is the average price in the Technology sector?”

“Explain Tesla’s stock price in simple terms”

# Current Limitations

Uses static stock data (demo purpose)

No authentication

No real-time streaming prices

SQLite used instead of cloud DB

# Future Enhancements

Live market APIs (Alpha Vantage / Polygon)

RAG with financial reports (10-K, earnings)

Multi-agent architecture (Analyst, Risk Agent)

Portfolio tracking

FastAPI backend

Dockerized deployment

Cloud database (PostgreSQL)

# Author

Kashmala Musarrat Ali
LLM & Agentic AI Engineer
Specializing in:

Generative AI

LLM applications

AI agents

Data engineering & analytics

Deterministic analytics

Safe, explainable outputs

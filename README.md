---
title: AI Multi-Agent System
emoji: ⚡
colorFrom: indigo
colorTo: blue
sdk: docker
app_port: 7860
pinned: false
---

# AI Multi-Agent System

An advanced orchestration platform where specialized AI agents work together to solve complex research and coding tasks.

## Features
- **Research Agent**: Deep exploration and information gathering.
- **Coding Agent**: Automated Python solution generation.
- **Summary Agent**: Clear and concise final explanations.
- **Modern UI**: Dark-themed dashboard built with Streamlit.

## How to Run Locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file and add your `COHERE_API_KEY`.
4. Run the app: `streamlit run app.py`

## Deployment
This project is configured for deployment on **Hugging Face Spaces**. 
Ensure you set the `COHERE_API_KEY` in the Space's Secret settings.

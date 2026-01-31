# 🤖 AI Code Review & Rewrite Agent

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688.svg)](https://fastapi.tiangolo.com/)
[![LLM](https://img.shields.io/badge/LLM-Llama_3.3_70B-orange.svg)](https://groq.com/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind-CSS-38B2AC.svg)](https://tailwindcss.com/)

An advanced AI-powered application designed to transform code quality through real-time analysis and automated refactoring. [cite_start]This tool identifies bugs, security vulnerabilities, and performance bottlenecks, providing instant, production-ready code rewrites[cite: 7, 10, 12].

---

## 🌟 Key Features
* [cite_start]**Ultra-Fast Inference:** Leverages Groq’s Llama 3.3 70B model for near-instant code reviews[cite: 8, 73].
* [cite_start]**Multi-Language Support:** Analyzes Python, Java, C++, and JavaScript with semantic accuracy[cite: 16].
* [cite_start]**Automated Refactoring:** Features a dedicated "Rewrite" function to optimize and clean code automatically[cite: 10, 52].
* [cite_start]**Severity Categorization:** Issues are ranked by priority: Critical, High, Medium, and Low[cite: 49].
* [cite_start]**Modern UI/UX:** Responsive interface built with Tailwind CSS, featuring side-by-side code comparisons[cite: 11, 54].

---

## 📂 Project Structure
[cite_start]The project follows a clean, modular architecture to ensure scalability and ease of deployment[cite: 94].

```text
CODEREVGENAI/
├── backend/                # FastAPI Application logic
│   ├── .env                # Private API configuration
[cite_start]│   ├── main.py             # Server endpoints & LLM integration [cite: 102]
[cite_start]│   ├── requirements.txt    # Dependency manifest [cite: 103]
│   └── venv/               # Isolated Python environment
└── frontend/               # Web Interface
    [cite_start]├── index.html          # Main application dashboard [cite: 105]
    └── login.html          # User authentication page [cite: 106]

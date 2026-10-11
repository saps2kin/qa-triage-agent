# QA Triage & Test Case Agent

An enterprise-ready Python and Streamlit web application designed to automate software quality assurance cycles. It processes unstructured bug reports and customer feedback into structured, standardized JSON triage artifacts and test cases.

## 🚀 Live Demo
Access the live deployed application here: **[🔗 Triage Agent on Streamlit Cloud](https://triage-agent.streamlit.app)** *(or insert your custom URL)*

---

## 🛠️ Tech Stack & Architecture
* **Frontend / UI:** [Streamlit](https://streamlit.io/)
* **Core Logic:** Python (Standard Library / Modular Backend)
* **Version Control:** Git & GitHub
* **Cloud Hosting:** Streamlit Community Cloud

### Project Structure
```text
qa-triage-agent/
│
├── agent.py            # Core backend logic for parsing and JSON generation
├── app.py              # Streamlit web interface and file handling
├── requirements.txt    # Python dependencies for deployment
├── .gitignore          # Excludes temporary cache, .env, and local outputs
├── inputs/             # Directory for sample raw bug reports & text files
└── outputs/            # Local directory for generated JSON triage reports
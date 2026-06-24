# 🗄️ SQL Query Generator

A bilingual AI-powered tool that converts plain text into SQL queries instantly — supporting both Arabic and English.

## 🔗 Live Demo
[Try it here](https://sql-generator-98hkrsqcnfjzbmjuu6mrdg.streamlit.app/)

## 💡 What it does
Instead of writing SQL manually, you just describe what data you need in plain Arabic or English
— and the app generates the SQL query with a full line-by-line explanation in your language.

Perfect for:
- ✅ Managers who need data insights without knowing SQL
- ✅ Professionals who want to save time
- ✅ Students who are still learning

## ⚙️ How it works
1. Type your request in Arabic or English
2. Select your database type (MySQL, PostgreSQL, SQL Server, SQLite)
3. Get the SQL query instantly
4. Read a clear explanation of every line in your own language

## 🛠️ Built With
- Python
- Streamlit
- Groq API (LLaMA 3.3 70B)

## 🚀 Run Locally
```bash
git clone https://github.com/Khaledkhalmutairi/sql-generator.git
cd sql-generator
pip install -r requirements.txt
streamlit run app.py
```

## 🔐 Environment Variables
Create a `.streamlit/secrets.toml` file:
```
GROQ_API_KEY = "your-groq-api-key"
```

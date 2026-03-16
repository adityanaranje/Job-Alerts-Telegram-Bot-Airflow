
# 🤖 AI/ML Job Alerts Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Airflow](https://img.shields.io/badge/Apache%20Airflow-3.0-orange)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automated-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

An automated pipeline that fetches **AI / ML job postings**, evaluates how well they match a resume using an LLM chain, stores results in Google Sheets, and sends relevant jobs via Telegram notifications.

This project demonstrates **Data Engineering + LLM + Automation** concepts useful for **ML Engineer / GenAI / Data roles**.

---

# 🚀 Features

- 🔎 Fetch AI/ML jobs from Google Jobs API (SerpAPI)
- 🧠 Resume–Job matching using LLM chain
- 📊 Store jobs in Google Sheets
- 🛑 Prevent duplicate jobs using `job_id`
- 📩 Send alerts via Telegram bot
- ⏰ Automated daily execution using GitHub Actions
- 🗂 Pipeline structure similar to Airflow DAG workflow

---

# 🧩 Architecture

```
            Job Search API (SerpAPI)
                       │
                       ▼
                Fetch Job Listings
                       │
                       ▼
           LLM Processing & Resume Matching
                       │
                       ▼
              Remove Duplicate Jobs
                       │
                       ▼
            Store Jobs → Google Sheets
                       │
                       ▼
             Filter Unsent Job Alerts
                       │
                       ▼
                Telegram Notification
```

---

# 📂 Project Structure

```
Job-Alerts-Telegram-Bot-Airflow
│
├── scripts/
│   ├── fetch_jobs.py
│   ├── store_to_sheets.py
│   └── send_telegram.py
│
├── utils/
│   └── sheets_client.py
│
├── job_pipeline.py
├── requirements.txt
│
└── .github/
    └── workflows/
        └── job_pipeline.yml
```

---

# ⚙️ Pipeline Workflow

1️⃣ Fetch job listings for:

- AI ML Engineer  
- Data Scientist  
- Generative AI Engineer  

2️⃣ Clean and shorten job descriptions to reduce token usage.

3️⃣ Pass job information + resume into LLM chain to extract:

- title
- experience
- salary
- job type
- match score

4️⃣ Remove duplicate jobs using `job_id`.

5️⃣ Store new jobs in Google Sheets.

6️⃣ Send Telegram alerts only for jobs where:

```
alert_sent = False
```

7️⃣ Mark alerts as sent in the sheet.

---

# 📊 Google Sheet Schema

| Column | Description |
|------|-------------|
job_id | Unique job identifier |
title | Job title |
company | Company name |
experience | Experience required |
location | Job location |
salary | Salary range |
job_type | Full-time / Contract |
posted_at | Job posting time |
fetched_at | Pipeline fetch time |
match_score | Resume match score |
description | Cleaned job description |
alert_sent | Boolean flag |

---

# 📨 Example Telegram Alert

```
🚀 New Job Match

🏢 Company: Zorba AI
💼 Role: Data Scientist
📍 Location: Hyderabad

⏰ Posted: 21 hours ago
💰 Salary: ₹13L–₹30L
📋 Job Type: Full-time
🎯 Match Score: 84%

🔗 Apply:
https://linkedin.com/...
```

---

# 🔑 Environment Variables

Store secrets in **GitHub Repository Secrets**.

```
SERPAPI_KEY
GOOGLE_CREDENTIALS
TELEGRAM_TOKEN
TELEGRAM_CHAT_ID
SHEET_ID
```

---

# ⏰ Automation

The pipeline runs automatically using **GitHub Actions**.

Schedule:

```
Daily at 09:00 AM IST
```

Cron configuration:

```
30 3 * * *
```

(UTC time used by GitHub Actions)

---

# 📦 Installation

Clone repository

```
git clone https://github.com/yourusername/job-alert-pipeline.git
cd job-alert-pipeline
```

Install dependencies

```
pip install -r requirements.txt
```

Run pipeline manually

```
python job_pipeline.py
```

---

# 🧠 Technologies Used

- Python
- Apache Airflow style DAG pipeline
- LangChain LCEL
- SerpAPI
- Google Sheets API
- Telegram Bot API
- GitHub Actions

---

# 🎯 Use Cases

- Automated job monitoring
- AI-powered resume matching
- Learning data pipelines
- Building production-style ML automation

---

# 📈 Future Improvements

- Vector embeddings for resume matching
- Ranking jobs by relevance
- Multi-source job scraping (LinkedIn, Indeed)
- Dashboard for job analytics
- Email notifications

---

# 👨‍💻 Author

Aditya Naranje

AI / ML Engineer | GenAI Developer

---

# ⭐ Support

If you find this project useful:

⭐ Star the repository  
🍴 Fork the project  
📢 Share with others

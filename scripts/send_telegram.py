import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
from scripts.store_to_sheets import mark_job_sent

def is_valid_url(url):
    if not url:
        return False
    return url.startswith("http")

def send_alerts(data):

    top_jobs = data.sort_values("Match Score", ascending=False)

    for index, job_data in top_jobs.iterrows():

        msg = f"""
        🚨 {job_data['Title']} - {job_data['Company']}

        📍 Location: {job_data['Location']}
        💼 Experience: {job_data['Experience']}
        Salary
        💰 Salary: {job_data['Salary']}

        ⏰ Posted: {job_data['Job Posted']}
        🧑‍💻 Job Type: {job_data['Job Type']}

        🎯 Resume Match: {job_data['Match Score']}%



        🧠 Job Description
        {job_data['Description']}
        """

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

        payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": msg
        }

        buttons = []
        if is_valid_url(job_data['Link']):
            buttons.append({"text": "Apply Now", "url": job_data['Link']})

        if buttons:
            payload["reply_markup"] = {
                    "inline_keyboard": [buttons]
            }

        requests.post(
            url, 
            json=payload
        )

        mark_job_sent(job_data['JOB ID'])

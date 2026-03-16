import pandas as pd
from datetime import datetime
from config import SERP_API_KEY, llm
from utils.resume_loader import load_resume
import serpapi
import pytz

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser


parser = JsonOutputParser()

prompt = ChatPromptTemplate.from_template(
    """
    Extract job information from the following data.

    extensions: {extensions}
    detected_extensions: {detected_extensions}
    title: {title}
    description: {description}
    resume : {resume}

    Return JSON with this structure:

    {{
    "title":"",
    "posted_at": "",
    "salary": "",
    "job_type": "",
    "description":"",
    "match_score":"",
    "experience":""
    }}

    Rules:
    - title = title of the job only (remove extra data from title if present)
    - posted_at = time since job was posted
    - salary = salary range
    - job_type = Full-time / Part-time / Contract
    - description = summary of description of the job
    - match_score = Score from 0–100 based on resume vs job description.
        Guidelines for match_score:
        - 85–100 → Excellent match (most required skills + experience match)
        - 70–84 → Good match (many skills match but some gaps)
        - 50–69 → Partial match (some relevant skills but missing key ones)
        - 30–49 → Weak match (few relevant skills or experience gap)
        - 0–29 → Poor match (mostly unrelated)
        
        Rules:
        - Do NOT give >85 unless resume strongly matches required skills and experience.
        - If key skills or experience are missing, keep score below 70.
        - Entry-level resume for senior role → below 50.
    - experience = years of experience required to apply for the job e.g. 2 years, 2+, 2-5 years
    - If a value is missing return "Not Specified"
    - Return ONLY valid JSON
    """
)

chain = prompt | llm | parser

ist = pytz.timezone("Asia/Kolkata")

formatted_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

resume_text = load_resume()



def fetch_jobs():

    client = serpapi.Client(api_key=SERP_API_KEY)

    roles = [
        "AI ML Engineer",
        "Data Scientist",
        "Generative AI Engineer"
    ]

    jobs = []

    for role in roles:

        results = client.search({
            "engine": "google_jobs",
            "location": "India",
            "google_domain": "google.co.in",
            "hl": "en",
            "gl": "in",
            "q": role,
            "fiters":"4 Days ago",
        })

        for job in results.get("jobs_results", []):

            job_id = job.get("job_id")

            description = job.get("description", "")

            if description:
                description = description[:1200]

            response = chain.invoke({
                "title": job.get("title"),
                "extensions": job.get("extensions", []),
                "detected_extensions": job.get("detected_extensions", {}),
                "description": description,
                "resume": resume_text
            })

            jobs.append({
                "job_id": job_id,
                "title": response.get("title"),
                "company": job.get("company_name"),
                "experience": response.get("experience"),
                "location": job.get("location"),
                "link": job.get("apply_options", [{}])[0].get("link"),
                "salary": response.get("salary"),
                "job_type": response.get("job_type"),
                "posted_at": response.get("posted_at"),
                "fetched_at": formatted_time,
                "alert_sent": False,
                "match_score": float(response.get("match_score", 0)),
                "description": response.get("description"),
                "search_role": role
            })

    df = pd.DataFrame(jobs)

    # Remove duplicate jobs
    df = df.drop_duplicates(subset=["job_id"])

    return df

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import os

import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from scripts.fetch_jobs import fetch_jobs
from scripts.store_to_sheets import store_jobs, get_jobs
from scripts.send_telegram import send_alerts


def pipeline():

    df = fetch_jobs()

    store_jobs(df)

    df = get_jobs()
    
    send_alerts(df)


with DAG(
    dag_id="job_alert_pipeline",
    start_date=datetime(2024,1,1),
    schedule="*/30 * * * *",
    catchup=False,
) as dag:

    run_pipeline = PythonOperator(
        task_id="job_pipeline",
        python_callable=pipeline
    )
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

if __name__ == "__main__":
    pipeline()

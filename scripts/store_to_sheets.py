from utils.sheets_client import get_sheet
import pandas as pd

def store_jobs(df):

    sheet = get_sheet()

    # Get existing sheet data
    existing_data = sheet.get_all_records()

    if existing_data:
        existing_df = pd.DataFrame(existing_data)
        existing_ids = set(existing_df["JOB ID"].astype(str))
    else:
        existing_ids = set()

    # Keep only jobs not already in sheet
    new_jobs = df[~df["job_id"].astype(str).isin(existing_ids)]

    if new_jobs.empty:
        return

    rows = new_jobs.values.tolist()

    sheet.append_rows(rows)


def get_jobs():
    sheet = get_sheet()

    data = sheet.get_all_records()

    data = pd.DataFrame(data)

    df = data[data["Alert Sent"] == 'FALSE']

    return df

def mark_job_sent(job_id):

    sheet = get_sheet()

    data = sheet.get_all_records()

    for i, row in enumerate(data):

        if row["JOB ID"] == job_id:

            sheet_row = i + 2   # +2 because header row = 1

            alert_col = 11       # column number of alert_sent

            sheet.update_cell(sheet_row, alert_col, 'TRUE')

            print(f"Updated job {job_id} as sent")

            break
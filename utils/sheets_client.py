import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_SHEET_NAME
import os
import json


creds_dict = json.loads(os.getenv("GOOGLE_CREDENTIALS"))

def get_sheet():

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        creds_dict, scope
    )

    client = gspread.authorize(creds)

    sheet = client.open(GOOGLE_SHEET_NAME).sheet1

    return sheet

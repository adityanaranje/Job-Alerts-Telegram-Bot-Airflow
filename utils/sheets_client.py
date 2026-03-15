import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_SHEET_NAME
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CREDENTIAL_PATH = os.path.join(BASE_DIR, "credentials.json")

creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

def get_sheet():

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIAL_PATH, scope
    )

    client = gspread.authorize(creds)

    sheet = client.open(GOOGLE_SHEET_NAME).sheet1

    return sheet
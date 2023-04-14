import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# defines key_file.json address
service_account_file = (
    r"EDIT"
)

creds = ServiceAccountCredentials.from_json_keyfile_name(service_account_file, scope)

client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open("EDIT")

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

records_data = sheet_instance.get_all_records()

records_df = pd.DataFrame.from_dict(records_data)

print(records_df.head())
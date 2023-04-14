import os
from dotenv import load_dotenv
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

spreadsheet_name =  os.getenv("SPREADSHEET_NAME")
path_position = os.getenv("PATH_POSITION")
key_file = os.getenv("KEY_FILE")

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def get_columns():
    # defines key_file.json address
    service_account_file = (
        key_file
    )

    creds = ServiceAccountCredentials.from_json_keyfile_name(service_account_file, scope)

    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet
    sheet = client.open(spreadsheet_name)

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(0)

    records_data = sheet_instance.get_all_records()

    records_df = pd.DataFrame.from_dict(records_data)
    
    columns = list(records_df.columns)
    
    return columns
   
def get_data(): 
    
    # defines key_file.json address
    service_account_file = (
        key_file
    )

    creds = ServiceAccountCredentials.from_json_keyfile_name(service_account_file, scope)

    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet
    sheet = client.open(spreadsheet_name)

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(0)

    records_data = sheet_instance.get_all_records()

    records_df = pd.DataFrame.from_dict(records_data)
    
    data = records_df.head()
    
    return data


# print(get_data())
# print(get_columns())
get_columns()
get_data()

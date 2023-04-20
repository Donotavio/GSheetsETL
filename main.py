import logging
from workers import db_connection
from workers import get_sheets_gs

logger = logging.getLogger(__name__)

def extract_load():
    data = get_sheets_gs.get_data(spreadsheet_name=input("Enter Google Sheets name: "))

    table_name = input("Enter table name: ")

    engine = db_connection.db_con()

    data_sql = data.to_sql(
        table_name, con=engine, if_exists="replace", index=False, schema="sheets"
    )

    return data_sql


if __name__ == "__main__":
    try:
        extract_load()
        print({"success": True})
    except: 
        print("ERROR!!!\nSheets not found.")
    

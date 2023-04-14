from workers import db_connection
from workers import get_sheets_gs

data = get_sheets_gs.get_data(spreadsheet_name=input("Enter Google Sheets name: "))

table_name = input("Enter table name: ")

engine = db_connection.db_con()

data.to_sql(table_name, con=engine, if_exists="replace", index=False, schema="sheets")

print("FIM!")

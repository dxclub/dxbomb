import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("ENTERGOOGLEAPICREDENTIALSNAMEHERE.json", scope)

client = gspread.authorize(creds)

sheet = client.open("ENTERGOOGLESHEETSNAMEHERE").sheet1

data = sheet.get_all_records()

pprint(data)
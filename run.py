import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales data from user
    """
    print('Please enter sales data from previous sales day')
    print('6 x Numbers, each seperates with commas... see below')
    print('"10,20,60,100,90"\n')

    data_str = input('Enter your data here:')
    print(f"You entered: {data_str}")

get_sales_data()
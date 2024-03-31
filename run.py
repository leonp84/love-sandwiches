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
    sales_data = data_str.split(',')



    validate_data(sales_data)
    print(f"You entered: {sales_data}")

def validate_data(values):
    """
    Validate Data by checking 6 values and all integers
    """
    print(values)
        if len(sales_data) != 6:
        print(len(sales_data))
        print('Wrong length! Quitting now')
        sales_data = []

    for i in sales_data:
        if not i.isdigit():
            print('Wrong Values! Not right! Quitting now... gonna have to repeat!')
            sales_data = []

get_sales_data()
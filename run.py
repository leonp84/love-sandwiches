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
    while True:
        print('===============================================')
        print('Please enter sales data from previous sales day')
        print('6 x Numbers, each seperates with commas... see below')
        print('"10,20,60,100,90"')
        print('===============================================')

        data_str = input('Enter your data here: ')
        sales_data = data_str.split(',')

        if validate_data(sales_data):
            print('Data is valid!')
            break
    
    return sales_data


def validate_data(values):
    """
    Validate Data by checking 6 values and all integers
    """
    if len(values) != 6:
        print(f"Wrong length of {len(values)}! Repeat!\n")
        return False

    for i in values:
        if not i.isdigit():
            print('Wrong Values! Not right! gonna have to repeat!\n')
            return False

    return True


def update_worksheet(worksheet, data):
    """
    Update specific worksheet
    """
    print(f'Updating {worksheet} worksheet...')
    s_worksheet = SHEET.worksheet(worksheet)
    print(f'Data being inserted: "{data}"')
    s_worksheet.append_row(data)
    print(f'{worksheet.capitalize()} Worksheet updated... \n')

def calculate_surplus_data():
    '''
    Let's calculate the suplus!
    '''
    print('Calculating Surplus...\n')
    stock = SHEET.worksheet('stock').get_all_values()
    sales = SHEET.worksheet('sales').get_all_values()

    new_data = []

    x = len(stock)-1

    for i in range(6):
        new_data.append(int(stock[x][i]) - int(sales[x][i]))
    
    return new_data


def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet('sales', sales_data)
    new_surplus_data = calculate_surplus_data()
    update_worksheet('surplus', new_surplus_data)

print('\nWelcome! Have a sandwich 🥪\n')
main()
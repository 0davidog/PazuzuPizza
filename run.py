# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pazuzu_pizza')


def display_pizzas():
    """
    Display the list of pre-made pizzas available.
    List is numbered and displayed without square brackets.
    """
    pizza_menu = SHEET.worksheet('pizza_menu')
    menu_list = pizza_menu.get_all_values()
    for i, pizza in enumerate(menu_list[1:]):
        pizza_str = ', '.join(pizza)
        print(f'{i + 1}: {pizza_str}')
    print('\n')
    option_select()

def convert_day():
    """
    Function takes todays day and converts it into a column reference.
    """
    day = datetime.now().strftime("%a")
    if day == "Mon":
        return "B"
    elif day == "Tue":
        return "C"
    elif day == "Wed":
        return "D"
    elif day == "Thu":
        return "E"
    elif day == "Fri":
        return "F"
    elif day == "Sat":
        return "G"
    elif day == "sun":
        return "H"  


def input_sales():
    """
    Function to input sales figures.
    """
    print(f'Sales figures for {datetime.now().strftime("%a, %d %B %Y")}\n')
    
    pizza_sales = SHEET.worksheet('pizza_sales')
    pizza_list = pizza_sales.col_values(1)
    
    for i, pizza in enumerate(pizza_list[1:]):
        while True:
            try:
                sold = int(input(f"Enter sales for {pizza}: "))
                pizza_sales.update(f"{convert_day()}{i + 2}", f"{sold}")
                break;
            except ValueError:
                print('Please enter a whole number')
        



def option_select():
    """"
    Select which function to use
    """
    print('Please select an option...')
    print('> 1: Display Pizza Menu')
    print('> 2: Input Sales')
    print('> 3: Input Disposals')
    print('> 6: Exit\n')

    user_selection = input('Input Option Number: ')
    if user_selection == "1":
        print('\nDisplaying Pizza Menu...\n')
        display_pizzas()
    elif user_selection == "2":
        print('\nRecording sales...\n')
        input_sales()
        option_select()
    elif user_selection == "6":
        print('exit\n')    
    else:
        print('Please select valid option')
        print('Only the option number is required')
        option_select() 


print('Welcome to the Pazuzu Pizza App\n')

option_select()
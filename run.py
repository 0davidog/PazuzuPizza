# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
SHEET = GSPREAD_CLIENT.open('pazuzu_pizza')

print('Welcome to the Pazuzu Pizza App\n')

def display_pizzas():
    pizza_menu = SHEET.worksheet('pizza_menu')
    menu_list = pizza_menu.get_all_values()
    for pizza in menu_list[1:]:
        print(*pizza)
    print('\n')    
    option_select()

def option_select():
    print('Please select a function')
    print('> 1: Display Pizza Menu')
    print('> 2: Input Sales')

    user_selection = input('Function #: ')
    if user_selection == "1":
        print('Display Pizza Menu selected\n')
        display_pizzas()
    elif user_selection == "2":
        print('2 selected, good')
        option_select()
    else:
        print('Please select valid option')
        option_select() 

option_select()


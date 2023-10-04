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
    start_program()

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
                pizza_sales.update(f"{convert_day()}{i + 2}", f"{sold}", value_input_option='USER_ENTERED')
                break
            except ValueError:
                print('Please enter a whole number')
    print('\nThank you. Updating production plan for next week.\n')
    calculate_production_plan()
    print('Production plan updated succesfully.')
    start_program()            
        

def input_waste():
    """
    Function to record wasteage
    """
    print(f'Disposal figures for {datetime.now().strftime("%a, %d %B %Y")}\n')

    pizza_waste = SHEET.worksheet('pizza_disposals')
    disposal_list = pizza_waste.col_values(1)
    ingredient_disposal = disposal_list[1:16]
    pizza_disposal = disposal_list[16:30]

    print('Please select an option...')
    print('> 1: Ingredients Disposal')
    print('> 2: Pizza Disposal')
    print('> 3: Exit\n')

    user_waste_selection = input('Input Option Number: ')
    if user_waste_selection == "1":
        print('\nRecording pizza ingredient disposals...\n')
        for i, ingredient in enumerate(ingredient_disposal):
            while True:
                try:
                    disposal = int(input(f"Enter disposal number for {ingredient}: "))
                    pizza_waste.update(f"B{i + 2}", f"{disposal}", value_input_option='USER_ENTERED')
                    break
                except ValueError:
                    print('Please enter a whole number')
        print('\n')            
        input_waste()            
    elif user_waste_selection == "2":
        print('\nRecording pre-made pizza disposals...\n')
        for i, pizza in enumerate(pizza_disposal):
            while True:
                try:
                    disposal = int(input(f"Enter disposal number for {pizza}: "))
                    pizza_waste.update(f"B{i + 17}", f"{disposal}", value_input_option='USER_ENTERED')
                    break
                except ValueError:
                    print('Please enter a whole number')
        print('\n')            
        input_waste()            
    elif user_waste_selection == "3":
        start_program()
    else:
        print('Please select valid option')
        print('Only the option number is required')
        input_waste()


def calculate_production_plan():
    """
    Function to calculate and update production plan.
    Takes the value of todays pizza sales and adds 10%.
    Updates number of pizzas to be made for same day.
    """
    pizza_sales = SHEET.worksheet('pizza_sales')
    pizza_production = SHEET.worksheet('pizza_production')

    pizza_list = pizza_sales.col_values(1)

    for i, pizza in enumerate(pizza_list[1:]):
        sale = int(pizza_sales.acell(f"{convert_day()}{i + 2}").value)
        target = sale * 1.1
        pizza_production.update(f'{convert_day()}{i + 2}', f"{round(target)}", value_input_option='USER_ENTERED')
    

def display_producion_plan():
    """
    Function to view todays production plan
    """
    pizza_production = SHEET.worksheet('pizza_production')
    pizza_list = pizza_production.col_values(1)
    print(f'Production plan for {datetime.now().strftime("%a, %d %B %Y")}\n')
    
    for i, pizza in enumerate(pizza_list[1:]):
        print(f'{pizza}: {pizza_production.acell(f"{convert_day()}{i + 2}").value}')

    start_program()
    

def option_select():
    """"
    Select which function to use
    """
    print('Please select an option...')
    print('> 1: Display Pizza Menu')
    print('> 2: Input Sales')
    print('> 3: Input Disposals')
    print('> 4: View Production Plan')
    print('> 6: Exit\n')

    user_selection = input('Input Option Number: ')
    if user_selection == "1":
        print('\nDisplaying Pizza Menu...\n')
        display_pizzas()
    elif user_selection == "2":
        print('\nRecording sales...\n')
        input_sales()
        start_program()
    elif user_selection == "3":
        print('\nRecording waste...\n')
        input_waste()
    elif user_selection == "4":
        print('\nDisplaying Production Plan...\n')
        display_producion_plan()
    elif user_selection == "6":
        print('exit\n')    
    else:
        print('Please select valid option')
        print('Only the option number is required')
        start_program() 


def start_program():
    """
    Activate Functions
    """
    option_select()

print('\nWelcome to the Pazuzu Pizza App\n')

start_program()


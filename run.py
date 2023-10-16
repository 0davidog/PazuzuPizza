# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Module imports
import sys
import time
import gspread
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from google.oauth2.service_account import Credentials
from datetime import datetime
import colorama
from colorama import Fore
import pyfiglet

# Code to access gspread and google drive from love-sandwiches walkthough project

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pazuzu_pizza')

# End of Love-Sandwiches walkthrough code


def display_pizzas():
    """
    Display the list of pre-made pizzas available.
    List is pulled from google sheets, ignoring first cell in column.
    For each item in the list item is numbered and printed without square brackets.
    option_select function is then called to return user to menu.
    """
    pizza_menu = SHEET.worksheet('pizza_menu')
    menu_list = pizza_menu.get_all_values()
    print('\n')
    for i, pizza in enumerate(menu_list[1:]):
        pizza_str = ', '.join(pizza)
        time.sleep(0.5)
        print(f'{i + 1}: {pizza_str}')
    time.sleep(0.5)    
    print('\n')
    time.sleep(0.5)
    input("Press Enter to continue...\n")
    option_select()


def convert_day():
    """
    Function imports todays day from python's datetime module.
    Then converts it into a letter for use as column reference.
    This function will be called within other functions.
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
    elif day == "Sun":
        return "H"


def input_sales():
    """
    Function to input sales figures.
    Imports pizza_sales worksheet from google sheets.
    For each product listed the user is asked to input sales figure.
    Input is then added to spreadsheet.
    """
    time.sleep(0.5)
    print(
        f'\nSales figures for {datetime.now().strftime("%a, %d %B %Y")}\n'
        )
    
    pizza_sales = SHEET.worksheet('pizza_sales')
    pizza_list = pizza_sales.col_values(1)
    
    for i, pizza in enumerate(pizza_list[1:]):
        while True:
            try:
                time.sleep(0.5)
                sold = int(input(f"Enter sales for {pizza}: \n"))
                pizza_sales.update(
                    f"{convert_day()}{i + 2}", 
                    f"{sold}", 
                    value_input_option='USER_ENTERED'
                    )
                break
            except ValueError:
                time.sleep(0.5)
                print('Please enter a whole number')
    time.sleep(0.5)
    print('\nThank you. Updating production plan for next week...\n')
    calculate_production_plan()
    print('Production plan updated succesfully.\n')
    time.sleep(0.5)
    input("Press Enter to continue...\n")
    option_select()

def input_waste():
    """
    Function to record waste.
    Pulls data from spreadsheet to form list.
    Ask user to enter disposal figure for each item.
    Update spreadsheet with input.
    """
    print(f'\nDisposal figures for {datetime.now().strftime("%a, %d %B %Y")}\n')

    pizza_waste = SHEET.worksheet('pizza_disposals')
    pizza_stock = SHEET.worksheet('pizza_stock')
    disposal_list = pizza_waste.col_values(1)
    ingredient_disposal = disposal_list[1:]
    time.sleep(0.5)
    print('\nRecording pizza ingredient disposals...\n')
    for i, ingredient in enumerate(ingredient_disposal):
        while True:
            try:
                time.sleep(0.5)
                disposal = int(input(f"Enter disposal number for {ingredient}: "))
                pizza_waste.update(
                    f"B{i + 2}", f"{disposal}", value_input_option='USER_ENTERED'
                    )
                current_stock = int(pizza_stock.acell(f"B{i + 2}").value)
                pizza_stock.update(
                    f"B{i + 2}", f"{current_stock - disposal}", value_input_option='USER_ENTERED')
                break
            except ValueError as e:
                time.sleep(0.5)
                print(f'Invalid entry: {e} Please enter a whole number\n')
    time.sleep(0.5)
    input("Press Enter to continue...\n")
    option_select()


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
        pizza_production.update(
            f'{convert_day()}{i + 2}', 
            f"{round(target)}", 
            value_input_option='USER_ENTERED'
            )


def display_producion_plan():
    """
    Function to view todays production plan.
    Pulls production plan from google sheet based on day of the week.
    """
    pizza_production = SHEET.worksheet('pizza_production')
    pizza_list = pizza_production.col_values(1)
    time.sleep(0.5)
    print(f'\nProduction plan for {datetime.now().strftime("%a, %d %B %Y")}\n')
    
    for i, pizza in enumerate(pizza_list[1:]):
        try:
            cell_value = pizza_production.acell(f"{convert_day()}{i + 2}").value
            time.sleep(0.5)
            print(f'{pizza}: {cell_value}')
        except Exception as e:
            time.sleep(0.5)
            print(f'Error: An unexpected error occurred - {e}')
    time.sleep(0.5)
    input("Press Enter to continue...\n")
    option_select()


class Pizza:
    """
    Class of pizza.
    Forms a description/recipie using given data.
    """
    def __init__(self, kind, size, topping):
        self.kind = kind
        self.size = size
        self.topping = topping

    def desciption(self):
        """
        Return the pizza recipie to be printed.
        """
        return f"\n{self.size} {self.kind} recipie:\n{self.topping}\n"
    

def select_pizza_recipie_size():
    """
    Function to select a pizza recipie to view.
    """
    pizza_recipie = SHEET.worksheet('pizza_recipie')
    pizza_list = pizza_recipie.col_values(1)
    time.sleep(0.5)
    print('\nPlease select a size:\n')
    time.sleep(0.5)
    print('> Small (s)')
    time.sleep(0.5)
    print('> Large (l)\n')
    try:
        size_chosen = input('Choose s / l:\n')
        if size_chosen == "s":
            time.sleep(0.5)
            print('Please select a pizza')
            for i, pizza in enumerate(pizza_list[1:8]):
                time.sleep(0.5)
                print(f'> {i}: {pizza}')
        elif size_chosen == "l":
            time.sleep(0.5)
            print('\nPlease select a pizza:')
            for i, pizza in enumerate(pizza_list[8:15]):
                time.sleep(0.5)
                print(f'> {i + 7}: {pizza}')
        else:
            time.sleep(0.5)
            print("\nPlease enter either 's' or 'l' in lower case.\n")
            select_pizza_recipie_size()                
    except ValueError as e:
        time.sleep(0.5)
        print(f'\nInvalid entry: {e} Please the letter s or l\n')
    select_pizza_recipie()    

def select_pizza_recipie():     
    try:
        pizza_chosen = int(input('\nPlease select a pizza by number:\n'))
        if pizza_chosen <= 13:
            build_pizza_recipie(pizza_chosen)
            return pizza_chosen
        else:
            time.sleep(0.5)
            print('\nPlease select a number between 1 and 13\n')
            select_pizza_recipie()
    except ValueError as e:
        time.sleep(0.5)
        print(f'\nInvalid entry: {e} Please enter option as whole number.\n')


def build_pizza_recipie(pizza_num):
    """
    Function
    """
    
    pizza_recipie_list = SHEET.worksheet('pizza_recipie')
    pizza_dictionary = pizza_recipie_list.get_all_records()
    pizza_toppings = []
    
    for key, value in pizza_dictionary[pizza_num].items():
        if value == 0:
            pass
        elif key == 'Pizza':
            pass
        elif key == 'Size':
            pass    
        else:
            pizza_toppings.append(f"{value} {key}")
    
    toppings_str = ', \n'.join(pizza_toppings)
    pizza_recipie = (Pizza(f'{pizza_dictionary[pizza_num]["Pizza"]}', f'{pizza_dictionary[pizza_num]["Size"]}', f'{toppings_str}'))    
    time.sleep(0.5)
    print(pizza_recipie.desciption())
    time.sleep(0.5)
    input("\nPress Enter to continue...\n")
    option_select()


def weekly_delivery():
    day = datetime.now().strftime("%a")
    if day == "Mon":
        delivery()


def delivery():
    pizza_stock = SHEET.worksheet('pizza_stock')
    pizza_delivery = SHEET.worksheet('pizza_delivery')
    stock_list = pizza_delivery.col_values(1)
    for i, stock in enumerate(stock_list[1:]):
        delivery_value = int(pizza_delivery.acell(f'B{i + 2}').value)
        current_stock = int(pizza_stock.acell(f'B{i + 2}').value)
        if current_stock >= delivery_value:
            print('\nNOTICE: No weekly delivery received.')
            time.sleep(0.5)
            break
        else:    
            pizza_stock.update(f'B{i + 2}', f'{current_stock + delivery_value}', value_input_option='USER_ENTERED')
            print('\nNOTICE: Weekly delivery has been received.')
            time.sleep(0.5)
            print('Stock list updated.')


def option_select():
    """"
    Function acts as main-menu
    Ask user to select which function to use.
    Use if statement to activate chosen function.
    """
    time.sleep(0.5)
    print('\nPlease select an option...\n')
    time.sleep(0.5)
    print('> 1: Display Pizza Menu')
    time.sleep(0.5)
    print('> 2: Input Sales')
    time.sleep(0.5)
    print('> 3: Input Disposals')
    time.sleep(0.5)
    print('> 4: View Production Plan')
    time.sleep(0.5)
    print('> 5: View Pizza Recipie')
    time.sleep(0.5)
    print('> 6: Exit\n')
    time.sleep(0.5)
    user_selection = input('Input Option Number: \n')
    try:
        if user_selection == "1":
            time.sleep(0.5)
            print('\nDisplaying Pizza Menu...')
            loading_animation()
            display_pizzas()
        elif user_selection == "2":
            time.sleep(0.5)
            print('\nRecording sales...')
            loading_animation()
            input_sales()
            option_select()
        elif user_selection == "3":
            time.sleep(0.5)
            print('\nRecording waste...')
            loading_animation()
            input_waste()
        elif user_selection == "4":
            time.sleep(0.5)
            print('\nDisplaying Production Plan...')
            loading_animation()
            display_producion_plan()
        elif user_selection == "5":
            time.sleep(0.5)
            print('\nDisplaying Recipie...')
            loading_animation()
            select_pizza_recipie_size()    
        elif user_selection == "6":
            time.sleep(0.5)
            print('\nExiting program...')
            loading_animation()
            time.sleep(0.5)
            print('\nThank you for using the Pazuzu Pizza App.\n')
            time.sleep(0.5)
            sys.exit('Select [Run Program] button at the top to restart.\n')
        else:
            time.sleep(0.5)
            print('Please select valid option')
            time.sleep(0.5)
            print('Only the option number is required')
            time.sleep(0.5)
            option_select()
    except ValueError as e:
        time.sleep(0.5)
        print(f'Invalid entry: ({e}). Only the option number is required\n')   


def loading_animation():
    waiting = '\n***\n'
    for char in waiting:
        time.sleep(0.5)
        sys.stdout.write(Fore.GREEN + char)
        sys.stdout.flush()


def intro():
    """
    Function displays title and intro messages
    """
    time.sleep(1)
    loading_animation()
    time.sleep(1)
    title = pyfiglet.figlet_format("Pazuzu Pizza") 
    print(title) 
    time.sleep(2)
    print('Welcome to the Pazuzu Pizza App\n')
    time.sleep(1)
    input("Press Enter to continue...")
    time.sleep(1)
    loading_animation()
    time.sleep(1)


def start_program():
    """
    Activate Functions
    """
    intro()
    weekly_delivery()
    option_select()


start_program()

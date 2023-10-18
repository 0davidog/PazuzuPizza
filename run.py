# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Module imports
import sys
import time
import maskpass
import gspread
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from google.oauth2.service_account import Credentials
from datetime import datetime
import colorama
from colorama import Fore
from colorama import Style
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

def green_text():
    """
    Function turns command line text green via colorama module.
    Call prior to a print statement or typing_animation.
    """
    print(Fore.GREEN)


def red_text():
    """
    Function turns command line text red via colorama module.
    Call prior to a print statement or typing_animation.
    """
    print(Fore.RED)


def reset_color():
    """
    Function resets command line text via colorama module.
    Call after a coloured print statement or typing_animation.
    """
    print(Style.RESET_ALL)


def typing_animation(text, timing):
    """
    Function creates a short animation to represent text typed in real-time.
    """
    for char in text:
        time.sleep(timing)
        sys.stdout.write(char)
        sys.stdout.flush()


def intro():
    """
    Function displays title and intro messages
    """
    time.sleep(1)
    typing_animation('\n***\n', 0.5)
    time.sleep(1)
    title = pyfiglet.figlet_format("Pazuzu Pizza") 
    print(title)
    time.sleep(2)
    typing_animation('Welcome to the Pazuzu Pizza App\n', 0.1)
    time.sleep(1)
    green_text()
    typing_animation("Press Enter to continue...", 0.1)
    input('\n')
    reset_color()
    time.sleep(1)
    typing_animation('***\n', 0.5)
    time.sleep(1)


class Employee:
    """
    Creates class of employee to represent the user.

    Attributes
    ----------
    username = str
        Employee username. Checked against worksheet.
    password = str
        Employee password. Checked against worksheet.

    Methods
    -------
    validate_login
        Fetch data from 'employees' worksheet.
        Establish relevant columns for username and password.
        Check if username exists in username column.
        check if password exists in password column.
        Check if username and password are on same row.
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate_login(self):
        employee_database = SHEET.worksheet('employees')
        usernames = employee_database.col_values(1)[1:]
        passwords = employee_database.col_values(2)[1:]
        if self.username in usernames:
            if self.password in passwords:
                user_cell = employee_database.find(self.username)
                pass_cell = employee_database.find(self.password)
                if pass_cell.row == user_cell.row:
                    green_text()
                    print('LOGIN SUCCESSFUL')
                    reset_color()
                    typing_animation(f'Welcome {self.username}.', 0.1)
                else:
                    red_text()
                    print('LOGIN FAILED: Please check username and password.')
                    reset_color()
                    login()
            else:
                red_text()
                print('INCORECT PASSWORD')
                reset_color()
                login()
        else: 
            red_text()
            print('USER NOT RECOGNISED')
            reset_color()
            login()


def login():
    """
    Function for login
    Ask for user input USERNAME
    Ask for user input PASSWORD (input hidden by maskpass)
    send login_info as username, password to Employee class
    validate username and password with class method.
    """
    green_text()
    typing_animation('Please enter your colleague login:\n', 0.1)
    username = input('USERNAME:\n')
    password = maskpass.askpass(prompt='PASSWORD:\n', mask="*")
    reset_color()
    login_info = Employee(username, password)
    Employee.validate_login(login_info)


def display_pizzas():
    """
    Display the list of pre-made pizzas available.
    List is pulled from google sheets, ignoring first cell in column.
    For each item in the list item is numbered and printed without square brackets.
    option_select function is then called to return user to menu.
    """
    pizza_menu = SHEET.worksheet('pizza_menu')
    menu_list = pizza_menu.get_all_values()
    typing_animation('\n', 0.1)
    for i, pizza in enumerate(menu_list[1:]):
        pizza_str = ', '.join(pizza)
        time.sleep(0.5)
        print(f'{i + 1}: {pizza_str}')
    time.sleep(0.5)    
    typing_animation('\n', 0.1)
    time.sleep(0.5)
    green_text()
    typing_animation("Press Enter to continue...", 0.1)
    input('\n')
    reset_color()
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
                red_text()
                print('Please enter a whole number')
                reset_color()
    time.sleep(0.5)
    print('\nThank you. Updating production plan for next week...\n')
    calculate_production_plan()
    typing_animation('Production plan updated succesfully.\n', 0.1)
    time.sleep(0.5)
    green_text()
    typing_animation("Press Enter to continue...", 0.1)
    input('\n')
    reset_color()
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
                red_text()
                print(f'Invalid entry: {e} Please enter a whole number\n')
                reset_color()
    time.sleep(0.5)
    green_text()
    typing_animation("Press Enter to continue...", 0.1)
    input('\n')
    reset_color()
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
    print list. e.g.
    "Mozzarella 10
    Pepperoni 13"
    etc
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
            red_text()
            print(f'Error: An unexpected error occurred - {e}')
            reset_color()
    time.sleep(0.5)
    green_text()
    typing_animation("Press Enter to continue...", 0.1)
    input('\n')
    reset_color()
    option_select()


class Pizza:
    """
    
    Class of pizza.

    Attributes
    ----------
    kind = str
        The style of pizza e.g. 'Margheritta'.
    size = str
        This size of the pizza in either 'small' or 'large'.
    topping = str
        List of ingredients used in the style of pizza.

    Methods
    -------
    description
        Forms a description/recipie using given attributes.
            e.g. 
            "Large Margheritta recipie:
            1 large base
            2 passata
            3 mozarella"
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
    Fetch pizza_recipie worksheet
    Create list of column values from worsheet column 1
    Ask for user input of 's' or 'l'.
    Warn and re-ask if invalid or upper case.
    Print numbered list of column values
        first 7 if 's' selected
        next 7 if 'l' selected
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
        green_text()
        size_chosen = input('Choose s / l:\n')
        reset_color()
        if size_chosen == "s":
            time.sleep(0.5)
            print('Please select a pizza')
            for i, pizza in enumerate(pizza_list[1:8]):
                time.sleep(0.5)
                print(f'> {i}: {pizza}')
        elif size_chosen == "l":
            time.sleep(0.5)
            print('\nPlease select a pizza:')
            reset_color()
            for i, pizza in enumerate(pizza_list[8:15]):
                time.sleep(0.5)
                print(f'> {i + 7}: {pizza}')
        else:
            time.sleep(0.5)
            red_text()
            print("\nPlease enter either 's' or 'l' in lower case.\n")
            reset_color()
            select_pizza_recipie_size()                
    except ValueError as e:
        time.sleep(0.5)
        red_text()
        print(f'\nInvalid entry: {e} Please the letter s or l\n')
        reset_color()
    select_pizza_recipie()    


def select_pizza_recipie():
    """
    Ask user input for int.
    return input if within range asked.
    Warn and restart if outside of range or invalid input.
    """
    try:
        green_text()
        typing_animation('\nPlease select a pizza by number:', 0.1)
        pizza_chosen = int(input('\n'))
        reset_color()
        if pizza_chosen <= 13:
            build_pizza_recipie(pizza_chosen)
            return pizza_chosen
        else:
            time.sleep(0.5)
            red_text()
            print('\nPlease select a number between 1 and 13\n')
            reset_color()
            select_pizza_recipie()
    except ValueError as e:
        time.sleep(0.5)
        red_text()
        print(f'\nInvalid entry: {e} Please enter option as whole number.\n')
        reset_color()


def build_pizza_recipie(pizza_num):
    """
    Attribute
    ---------
    pizza_num = int
        received from select_pizza_recipie

    Fetch all pizza recipies from worksheet as list of dictionaries.
    Create new, blank list for pizza_toppings
    For every key in pizza_dictionary
        ignore if value is 0 
        ignore if Key is 'Pizza' or 'Size'
        add remaining value and key  pairs to pizza topping list
            e.g. "2 passata", "2 mozzarella".
    Join pizza_toppings list into a string var, 'toppings_str'.
    create var 'pizza_recipie' and send as attributes to Pizza class.
        (Pizza, Size, Toppings)
        e.g. "Mozarella", "large", "1 large base, 2 passata, 3 mozarella"
        indexed from dictionary via pizza_num attribute
    print desctiption() from Pizza class
    return to options
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
    green_text()
    typing_animation("Press Enter to continue...", 0.1)
    input('\n')
    reset_color()
    option_select()


def weekly_delivery():
    """
    Get day today from datetime
    Check if day is Mon
    Call delivery function if true
    """
    day = datetime.now().strftime("%a")
    if day == "Mon":
        delivery()


def delivery():
    """
    Fetch pizza_stock worksheet
    Fetch pizza_delivery worksheet
    Create list of values from col 1 of pizza_delivery
    for every item in stocklist
        fetch each delivery value
        fetch each stock value
        check if current stock value is greater than delivery value
            break if true
            add delivery value to stock value if false
    """
    pizza_stock = SHEET.worksheet('pizza_stock')
    pizza_delivery = SHEET.worksheet('pizza_delivery')
    stock_list = pizza_delivery.col_values(1)
    for i, stock in enumerate(stock_list[1:]):
        delivery_value = int(pizza_delivery.acell(f'B{i + 2}').value)
        current_stock = int(pizza_stock.acell(f'B{i + 2}').value)
        if current_stock >= delivery_value:
            red_text()
            print('\nNOTICE: No weekly delivery received.')
            reset_color()
            time.sleep(0.5)
            break
        else:    
            pizza_stock.update(f'B{i + 2}', f'{current_stock + delivery_value}', value_input_option='USER_ENTERED')
            red_text()
            print('\nNOTICE: Weekly delivery has been received.')
            time.sleep(0.5)
            print('Stock list updated.')
            reset_color()


def option_select():
    """"
    Function acts as main-menu
    Ask user to select which function to use.
    Use if statement to activate chosen function.
    Warn and restart if invalid input
    """
    time.sleep(0.5)
    typing_animation('\nPlease select an option...\n', 0.1)
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
    print('> 6: Exit')
    time.sleep(0.5)
    green_text()
    typing_animation('Input Option Number:', 0.1)
    user_selection = input('\n')
    reset_color()
    try:
        if user_selection == "1":
            time.sleep(0.5)
            print('\nDisplaying Pizza Menu...')
            typing_animation('\n***\n', 0.5)
            display_pizzas()
        elif user_selection == "2":
            time.sleep(0.5)
            print('\nRecording sales...')
            typing_animation('\n***\n', 0.5)
            input_sales()
            option_select()
        elif user_selection == "3":
            time.sleep(0.5)
            print('\nRecording waste...')
            typing_animation('\n***\n', 0.5)
            input_waste()
        elif user_selection == "4":
            time.sleep(0.5)
            print('\nDisplaying Production Plan...')
            typing_animation('\n***\n', 0.5)
            display_producion_plan()
        elif user_selection == "5":
            time.sleep(0.5)
            print('\nDisplaying Recipie...')
            typing_animation('\n***\n', 0.5)
            select_pizza_recipie_size()    
        elif user_selection == "6":
            time.sleep(0.5)
            typing_animation('\nExiting program...\n', 0.1)
            typing_animation('\n***\n', 0.5)
            time.sleep(0.5)
            typing_animation('\nThank you for using the Pazuzu Pizza App.\n', 0.1)
            time.sleep(0.5)
            red_text()
            sys.exit('Select [Run Program] button at the top to restart.\n')

        else:
            time.sleep(0.5)
            red_text()
            print('Please select valid option')
            time.sleep(0.5)
            print('Only the option number is required')
            time.sleep(0.5)
            reset_color()
            option_select()
    except ValueError as e:
        time.sleep(0.5)
        red_text()
        print(f'Invalid entry: ({e}). Only the option number is required\n')
        reset_color()  


def start_program():
    """
    Activate Functions in relevant order.
    """
    intro()
    login()
    weekly_delivery()
    option_select()


start_program()
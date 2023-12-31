# Pazuzu Pizza

![cover-image](https://github.com/0davidog/PazuzuPizza/assets/135815736/70556968-604b-48fc-b210-96d375a593c8)

Author: David C. O'Gara

Pazuzu Pizza is a command line application. Built in python, that enables users an easy way to keep up to date with sales and stock of their business. 
The app is created specifically for Pazuzu Pizza, a small pizza counter within a supermarket, and offers its users the ability to input sales data and wastage while automating their production plan and offering access to other useful information such as pizza recipes and menu lists.

- [Pazuzu Pizza](#pazuzu-pizza)
  * [Live Site](#live-site)
  * [Repository](#repository)
  * [Google Sheet](#google-sheet)
  * [User](#user)
  * [How to Use](#how-to-use)
  * [Features](#features)
    + [Login](#login)
    + [Option Selection](#option-selection)
    + [Display Menu](#display-menu)
    + [Input Sales](#input-sales)
    + [Today's Date](#today's-date)
    + [Input Disposals](#input-disposals)
    + [Delivery](#delivery)
    + [View Production Plan](#view-production-plan)
    + [View Pizza Recipe](#view-pizza-recipe)
  * [Future Features](#future-features)
    + [Pizza Stock](#pizza-stock)
  * [Planning Documentation](#planning-documentation)
  * [Data Model](#data-model)
  * [Libraries Used](#libraries-used)
  * [Testing](#testing)
    + [Manual test](#manual-test)
    + [Bugs](#bugs)
    + [Remaining Bugs](#remaining-bugs)
    + [Validator Testing](#validator-testing)
  * [Deployment](#deployment)
    + [Google Sheets API](#google-sheets-api)
    + [Gitpod](#gitpod)
    + [Heroku](#heroku)
  * [Credits](#credits)
    + [Mentor](#mentor)
    + [Author](#author)

## Live Site

[Pazuzu Pizza via Heroku](https://pazuzuz-pizza-b36de06442d6.herokuapp.com/)

## Repository

[Pazuzu Pizza Repository on Github](https://github.com/0davidog/PazuzuPizza)

## Google Sheet

[Pazuzu Pizza Google Sheet](https://docs.google.com/spreadsheets/d/1tuZHZiGloPHvjHOcF4cx2RZ7-4RQdUAO_I-zNRNlWxc/edit?usp=sharing)


## User

Pazuzu Pizza, is a small company that rents a counter in the corner of a larger supermarket. They pre-make and wrap a selection of pizzas in various styles and in one of two sizes (small or large). Customers can then purchase these pizzas cold to cook at home, or have them cooked in-store to take-away hot. The owner wants an application to simplify and in some ways automate some of the process of keeping track of sales and stock. The users of this app will be the staff members working on the counter on a given day.

## How to Use

![deployed-screen-01](https://github.com/0davidog/PazuzuPizza/assets/135815736/48196768-f1b3-4c84-8430-8d807d664021)

- The user is first asked to log in [more detail](#login).
    This is done by choosing one of these pre-made user accounts:
    ![employee-screen](https://github.com/0davidog/PazuzuPizza/assets/135815736/d9a05930-565f-4741-b385-d8340e20d0da)
- The user is then asked to select an option. This is done by inputting the option number. [more detail](#)
- Selecting 1. 'Display Menu' brings up a list of pizza styles the company makes. [more detail](#)
- Selecting 2. 'Input Sales' asks the user to input a number for each pizza. [more detail](#)
- Selecting 3. 'Input Disosals' asks user to input disposal number for each pizza ingredient. [more detail](#)
- Selecting 4. 'View Production Plan' shows the user to amount of pizzas to be made for today's date. [more detail](#)
- Selecting 5. 'View Pizza Recipe' asks the user to choose a pizza by number and then displays the recipe for the chosen pizza. [more detail](#)
  
## Features

### Login

After the introduction the user is asked to Log in to the app. Employees of Pazuzu Pizza are given log-in information by their management to prevent non-employees accessing and altering the information. This is stored in the employee database which is a worksheet named 'employees' in the Pazuzu_Pizza Google spreadsheet.

![worksheet-screen-08](https://github.com/0davidog/PazuzuPizza/assets/135815736/9ab88ba2-68b4-4695-99a0-5d4a04affb72)

First the user enters a username.

![deployed-screen-02](https://github.com/0davidog/PazuzuPizza/assets/135815736/ae3c8234-653a-4b4f-bec5-63f3e04e243e)

Followed by the password. 
The characters on the password input are hidden via the python module ['maskpass'](#maskpass).

![deployed-screen-03](https://github.com/0davidog/PazuzuPizza/assets/135815736/e1066b2d-3872-4a83-9aba-63a309a20a3e)

The app then retrieves the username and password and checks them against the 'employees' worksheet.
The username is checked first. If this doesn't exist on the worksheet a warning is given and the user is asked to enter the information again.

![deployed-screen-05](https://github.com/0davidog/PazuzuPizza/assets/135815736/62c52d83-c165-4118-93e9-43db72a46533)

Then, if the username is recognised but the password is not a different warning is issued and the user is asked to enter the information again.

![deployed-screen-06](https://github.com/0davidog/PazuzuPizza/assets/135815736/7dbc44b8-09f7-471b-926d-ac249db367a8)

This applies too if the inputs are left blank.

![deployed-screen-07](https://github.com/0davidog/PazuzuPizza/assets/135815736/f5f63ac4-eaaa-41b9-a7a8-59019dcbc2f0)

Once the username and password are entered correctly the user is taken to the main menu part of the app.

![deployed-screen-04](https://github.com/0davidog/PazuzuPizza/assets/135815736/c484add1-e190-41b5-a965-b82885b55edf)

### Option Selection

In the main menu the user is asked to select from a list of numbered options. Only the option number is required.

![deployed-screen-14](https://github.com/0davidog/PazuzuPizza/assets/135815736/8452af3f-ae94-4d32-9cc9-fcb76ea255bd)

If anything other than a whole number is entered a warning is given and the options are displayed again.

![deployed-screen-08](https://github.com/0davidog/PazuzuPizza/assets/135815736/1e6b3267-d57e-4f78-9033-53358a97349e)

This includes a blank input.

![deployed-screen-09](https://github.com/0davidog/PazuzuPizza/assets/135815736/f4919f5b-3115-4376-89b7-e25ab55fce45)

### Display Menu

Selecting option 1 displays a list of the pizza styles currently made by Pazuzu Pizza. This is drawn from the Pazuzu Pizza spreadsheet and the pizza_menu worksheet. This is included as reminder should any staff members need to check on the current list of pizza styles as changes may occur on a seasonal basis. 

![worksheet-screen-07](https://github.com/0davidog/PazuzuPizza/assets/135815736/2bc76bbb-5e1c-47be-9f28-98cf76c12d29)

The pizzas are then displayed in a numbered list.

![deployed-screen-10](https://github.com/0davidog/PazuzuPizza/assets/135815736/3f6905e4-8f45-4823-ac2a-4a8208404df7)

### Input Sales

Selecting option 2 will ask the user to input the days pizza sales one by one. This is to be done at the end of the shift when the business is closed for the day although they can be entered as many times as the user wishes should a mistake be made.

![deployed-screen-11](https://github.com/0davidog/PazuzuPizza/assets/135815736/1fe32434-cd6c-4bec-9a6e-fa35c77d9dbe)

If something other than a whole number is entered a warning is given and the user is asked to enter the number again.

![deployed-screen-13](https://github.com/0davidog/PazuzuPizza/assets/135815736/6dbeb55f-9656-479e-bb31-e8bf481d0b3e)

Once succesful the worksheet 'pizza_sales' will be updated in the column coresponding to the day of the week.

![worksheet-screen-01](https://github.com/0davidog/PazuzuPizza/assets/135815736/48231ff7-ab1f-46e8-944a-a1777fc3e222)

Side by side video demonstration [here](https://www.youtube.com/watch?v=KGoXKuTMRIo).

The 'pizza_production' worksheet will also be updated at the end of this function by calling the calculated_production_plan function. This takes today's sales, entered by the user and adds 10% to the number then rounded to an integer.

![worksheet-screen-02](https://github.com/0davidog/PazuzuPizza/assets/135815736/105f7d88-7541-4ab5-918a-f32ff9304cf4)

Side by side video demonstration [here](https://www.youtube.com/watch?v=P96URDFS7Tc).

### Today's Date

```
from datetime import datetime
```
The date used in these functions is determined by the datetime python module. The module is imported and then used to display the date at the start of some functions and also used to take today's day and translate it to an uppercase letter for use in determining the cell to update.
```
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
```
The formatted string literal bellow then used the letter returned from the convert_day function with an index determined in a for loop to create an A1 notation cell reference. In this instance the {sold} reference is the value input from the user entered in the input_sales function.
```
                pizza_sales.update(
                    f"{convert_day()}{i + 2}",
                    f"{sold}",
                    value_input_option='USER_ENTERED'
                    )
```

### Input Disposals

Selecting option 3 will ask the user to input the disposal numbers for each pizza ingredient. This is done at the end of the shift also, as there are often ingredients/toppings that reach the end of their allotted life or use by date and must be disposed of. The user is asked to input an integer of the amount of units of each ingredient. To the staff member of Pazuzu Pizza, this unit will relate to different quantities depending on the item. For example, 2 units may mean 2 4oz spoons of grated mozzarella, 2 2oz spoons of passata sauce or just 2 slices of pepperoni. The amount entered will be added to the 'pizza_disposal' worksheet.

![worksheet-screen-03](https://github.com/0davidog/PazuzuPizza/assets/135815736/ecaed384-d947-41e8-86d0-2481cce98e1b)

Side by side video demonstration [here](https://www.youtube.com/watch?v=LTGYZO7Mq24).
The number of disposals entered will also be subtracted from the values in the 'pizza_stock' worksheet.

![worksheet-screen-04](https://github.com/0davidog/PazuzuPizza/assets/135815736/023d5802-3936-4b08-b566-b58ef7e5008d)

Side by side video demonstration [here](https://www.youtube.com/watch?v=eNeWPodrs5A).

### Delivery

The 'pizza_stock' worksheet is also updated via a function called 'delivery'.
First, the function 'weekly_delivery', checks to see if today is Monday and proceeds to call the delivery function if this is true.
```
def weekly_delivery():
    """
    Get day today from datetime
    Check if day is Mon
    Call delivery function if true
    """
    day = datetime.now().strftime("%a")
    if day == "Mon":
        delivery()
```
The delivery function then adds a set amount of units to the 'pizza_stock' worksheet. These pre-set delivery units are accessed from the 'pizza_delivery' worksheet.
```
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
            pizza_stock.update(
                f'B{i + 2}', f'{current_stock + delivery_value}',
                value_input_option='USER_ENTERED'
                )
            red_text()
            print('\nNOTICE: Weekly delivery has been received.')
            time.sleep(0.5)
            print('Stock list updated.')
            reset_color()
```
![worksheet-screen-05](https://github.com/0davidog/PazuzuPizza/assets/135815736/390b9d44-1371-467f-ac7b-84019c4b5c6f)

### View Production Plan

Selecting option 4 displays for the user today's production plan. This tells the staff member how many pizzas to make for today based on last weeks sales with an aim to make and sell 10% more than last week.
This data is retrieved from the pizza_production worksheet with the column reference chosen through the [convert_day](#Today's-Date) function.

![Screenshot 2023-10-18 at 22-06-26 Python Terminal by Code Institute](https://github.com/0davidog/PazuzuPizza/assets/135815736/bc93d34c-b1d6-46d6-893d-9f8081d82293)

### View Pizza Recipe

Selecting option 5 displays a chosen pizza recipe for the user. Staff members can use this function to remind themselves what the standard is when creating pizzas, thus helping to create consistency in the pizzas produced by different colleagues.
Users are asked first to select the size of pizza they wish to view the recipe for. This is simply to reduce the size of the list and make it easy for the user to see the options within the limited view space. To choose, the user must input either 's' or 'l' in lower case letters.

![deployed-screen-15](https://github.com/0davidog/PazuzuPizza/assets/135815736/e600ecb8-515f-4a3e-9aaf-785243900ae7)

Choosing the size will then display a numbered list of pizzas.

Small:

![deployed-screen-16](https://github.com/0davidog/PazuzuPizza/assets/135815736/ce822f09-b528-4885-b096-9b9b39e55c6c)

Large:

![deployed-screen-18](https://github.com/0davidog/PazuzuPizza/assets/135815736/51569cca-de36-4d78-acad-7562c82ac69f)

Users are asked to input the number of the pizza they wish to view. The numbers are between 0 and 13. Doing so displays the pizza information.

Number 5 - Small Hot & Spicy:

![deployed-screen-17](https://github.com/0davidog/PazuzuPizza/assets/135815736/a2de7468-8c22-4bcf-bc49-e6b2cf711d0f)

Number 11 - Large Veggi Feast:

![deployed-screen-19](https://github.com/0davidog/PazuzuPizza/assets/135815736/3309746e-3e24-478f-a388-a163ab82e4fc)

Entering anything other than a whole number will result in a warning and the user will be asked to enter their choice again.

![deployed-screen-20](https://github.com/0davidog/PazuzuPizza/assets/135815736/1e3427ee-bfc7-4f97-94bc-d681262ea74e)

![deployed-screen-21](https://github.com/0davidog/PazuzuPizza/assets/135815736/f7203c54-b08a-443d-a574-b5897485a873)

## Future Features

Given production time and knowledge this app could provide a number of extra and more advanced features. Here is just a few:

- ### Pizza Stock
 
  The pizza stock list that keeps track of ingredients could be updated according the amound of pizzas made. This could be achieved by multiplying the amount of a particular topping needed for a pizza by the amount of that pizza produced. For example the amount of pepperoni used on a small pepperoni pizza is 8. If 15 small pepperoni pizzas are made that day than 120 slices of pepperoni will need to be subtracted from the stock of pepperoni. This will further simplify the stock ordering process for the company.

## Planning Documentation

Flow chart for 'input sales' function:
![input_sales drawio(1)](https://github.com/0davidog/PazuzuPizza/assets/135815736/aac4bf20-a68b-48a2-96d4-d4d7705c8ad2)

## Data Model

![class-table](https://github.com/0davidog/PazuzuPizza/assets/135815736/ed9c45eb-be93-4300-a97a-7a284a1b4afd)

## Libraries Used

- gspread
  - gspread was used to access and update google sheets.
- datetime [more detail](#Today's-Date)
- Google Drive
  - google drive credentials were needed to access google sheets.
- colorama
  - colorama Fore was used to change the text colour in various placed to add emphasis to inputs and warnings making the experience better for the customer.
  - colorama Style was used to reset any colour effects when needed.
- pyfiglet
  - pyfiglet provided the title font used to make the app introduction more eye catching.
- sys
  - sys was imported to set up the sys.exit function for the the user wishes to quit.
- maskpass
  - maskpass was installed to hide the user's password input.
- warnings [more detail](#Bugs)

## Testing

- [PEP8/CI Python Linter](#Validator-Testing)

- ### Manual test

Various manual test were done to check that the app works as expected. This includes deliberately entering the wrong inputs and checking the data given against the google sheets.

|Function|Intention|Action|No Terminal Error|Works as Expected|
|--------|---------|------|-----------------|-----------------|
|Login|Request and validate username and password.|Blank username input gives warning.<br>Wrong user name gives warning.<br>Blank password gives warning.<br>Wrong password gives warning. | [x] | [x] |
|Options|Request input of option number.|Blank entry gives warning.<br>String entered gives warning.<br>Float entered gives warning.| [x] | [x] |
|Display Menu|Display list of pizzas|Pizza list checked against worksheet.| [x] | [x] |
|Input Sales|Request input of whole number for each item.|String input gives warning.<br>Blank input gives warning. | [x] | [x] |
|Input Disposals|Request input of whole number for each item.|String input gives warning.<br>Blank input gives warning.| [x] | [x] |
|View Production Plan|Display list of pizzas for today's date.|List matches today. | [x] | [x] |
|View Pizza Recipe|1.Request input of s or l.<br>2.Request input of number between 1 and 13.|1.Blank input gives warning.<br>1.Wrong letter gives warning.<br>1.Number entered gives warning.<br>2.Number above 13 gives warning.<br>2.Blank input gives warning.| [x] | [x] |

### Bugs

Bug: A warning kept being printed the first time a google sheet was updated in a session. From some investigation it appeared the warning was for some changes being implimented in a future version of gspread. 

```
UserWarning: [Deprecated][in version 6.0.0]: method signature will change to: 'Worksheet.update(value = [[]], range_name=)' arguments 'range_name' and 'values' will swap, values will be mandatory of type: 'list(list(...))'
  warnings.warn(
```

Fix: The problem was solved by importing the warnings module and using it to ignore UserWarnings.

```
warnings.filterwarnings("ignore", category=UserWarning)
- (error occured because I had Sun in lowercase)
```

Bug: This error kept occuring when trying to update any of the day-based google sheets: 

```
Error: An unexpected error occurred - {'code': 400, 'message': "Unable to parse range: 'pizza_production'!NONE2", 'status': 'INVALID_ARGUMENT'}
```

Fix: It happened to be a Sunday when this error appeared and I found "Sun" in the convert_day function had been mistakenly written in lower case.

### Remaining Bugs

No known bugs remaining.

### Validator Testing

PEP8 validator passed with no issues.

![Screenshot 2023-10-18 at 16-38-28 CI Python Linter](https://github.com/0davidog/PazuzuPizza/assets/135815736/e9b9ecbd-7438-463e-a81b-9631506e103a)

[PEP8 Validator/ CI Python Linter](https://pep8ci.herokuapp.com/#)

## Deployment

### Google Sheets API

As mentioned throughout Pazuzu Pizza is connected to Google Sheets through an Application Programming Interface.

The Spreadsheet name is Pazuzu_Pizza. [link](https://docs.google.com/spreadsheets/d/1tuZHZiGloPHvjHOcF4cx2RZ7-4RQdUAO_I-zNRNlWxc/edit?usp=sharing)

Sheet names:
- pizza_sales
- pizza_production
- pizza_disposals
- pizza_stock
- pizza_delivery
- pizza_recipe
- pizza_menu
- employees

Instructions for setting this up:

(create google account use personal account as more secure
file - make a copy)

<details>
<summary>Method of setting up API</summary>
 
|Step|Screen|
|----|------|
|Head over to Google Cloud platform and log-in.|![api-screen-01](https://github.com/0davidog/PazuzuPizza/assets/135815736/cd0937c7-1e46-4f15-9862-5eca6c2bf0df)|
|Click 'Select a project'. Then 'New Project'.|![api-screen-02](https://github.com/0davidog/PazuzuPizza/assets/135815736/9b6e926e-40f6-471d-af2c-8f2b715be1d8)|
|Give your new project a name.|![api-screen-03](https://github.com/0davidog/PazuzuPizza/assets/135815736/f33eb7ed-fe7c-440c-b89f-335af915244d)|
|Click 'create'.|![api-screen-04](https://github.com/0davidog/PazuzuPizza/assets/135815736/7698070c-43a1-4194-8732-6b679b326b72)|
|Click 'Select Project'|![api-screen-05](https://github.com/0davidog/PazuzuPizza/assets/135815736/66f22aa0-887b-47b2-b4ae-451504d0b301)|
|You'll be taken to the dashboard.|![api-screen-06](https://github.com/0davidog/PazuzuPizza/assets/135815736/650c03e9-bc62-4bae-a272-fa3d2c76f9c6)|
|Using the side menu select 'APIs & Sservices' and then 'Library'|![api-screen-07](https://github.com/0davidog/PazuzuPizza/assets/135815736/7c14017d-7c30-46d7-b824-59e4702f03be)|
|You'll be taken to the API library.|![api-screen-08](https://github.com/0davidog/PazuzuPizza/assets/135815736/7ef21c5e-d9c2-45fb-8db7-4681f64ec1fb)|
|Search for 'Google Drive' and select 'Google Drive API'|![api-screen-09](https://github.com/0davidog/PazuzuPizza/assets/135815736/5a36954e-535a-480b-a498-3632039942e2)|
|Select 'Enable'|![api-screen-10](https://github.com/0davidog/PazuzuPizza/assets/135815736/f6e214e2-02d7-4d17-8fcf-ee4d7725a450)|
|In the next screen select 'Create Credentials'|![api-screen-11](https://github.com/0davidog/PazuzuPizza/assets/135815736/c5764f97-3e0a-4bb4-9cc2-594bf929f97a)|
|In 'which API are you using?', Select an API should be 'Google Drive API' and the data you'll be accessing is 'application data'. Click 'next'.|![api-screen-12](https://github.com/0davidog/PazuzuPizza/assets/135815736/1a9abe4f-c0b9-4f9e-8d71-bced08cfa4f6)|
|Choose a service account name and click 'create'|![api-screen-13](https://github.com/0davidog/PazuzuPizza/assets/135815736/59c98cb8-7d6b-4a94-bbdc-0f1ff13f844d)|
|In 'select a role' chose 'Basic' - 'Editor'.|![api-screen-14](https://github.com/0davidog/PazuzuPizza/assets/135815736/02841397-6766-4993-93ad-2b88948ec2e0)|
|Select 'continue'|![api-screen-15](https://github.com/0davidog/PazuzuPizza/assets/135815736/2fa6d779-fbc1-4cb3-840a-aa2a3efc3432)|
|You can leave this blank and click 'done'|![api-screen-16](https://github.com/0davidog/PazuzuPizza/assets/135815736/4294725a-8115-4311-b434-c4b8d09b4d99)|
|Select your service account on the next page.|![api-screen-18](https://github.com/0davidog/PazuzuPizza/assets/135815736/f0d233f2-8935-4dfd-9ffc-dad9b1033fba)|
|Then select the keys tab|![api-screen-19](https://github.com/0davidog/PazuzuPizza/assets/135815736/a5ff3ef0-ce79-40e6-9b27-0c0a374d3586)|
|Select 'add key'|![api-screen-20](https://github.com/0davidog/PazuzuPizza/assets/135815736/4034d595-6868-4c25-aae7-236ea54569bb)|
|Select 'create new key'|![api-screen-21](https://github.com/0davidog/PazuzuPizza/assets/135815736/f4185f0a-cb25-4c9e-8fb9-c5e18962f93a)|
|Select 'JSON' and click 'create'.|![api-screen-22](https://github.com/0davidog/PazuzuPizza/assets/135815736/ee8b4189-374d-4272-a208-dda6ffaa3066)|
|The json file will be saved to your computer|![api-screen-23](https://github.com/0davidog/PazuzuPizza/assets/135815736/98f1da80-a387-4f11-9219-4deb2803adee)|
|Back at the API library search for 'Google Sheets'|![api-screen-24](https://github.com/0davidog/PazuzuPizza/assets/135815736/1a8654d7-2eca-4071-b874-9649d8a525b7)|
|Simply select 'enable'|![api-screen-25](https://github.com/0davidog/PazuzuPizza/assets/135815736/0a9beeda-4a82-4c00-90bf-e5c3ba6ca430)|
|And the API will be enabled|![api-screen-26](https://github.com/0davidog/PazuzuPizza/assets/135815736/23744dbc-82f9-4982-aa82-960fbe7992c6)|
|Drag and drop the downloaded json file into your project folder. Rename it if you like (e.g. creds.json). Then access the file and copy the client email.|![api-screen-27](https://github.com/0davidog/PazuzuPizza/assets/135815736/450a685f-7016-439c-b726-81c1fd6c0951)|
|Then you can share you google sheet with your client email to allow access.|![api-screen-29](https://github.com/0davidog/PazuzuPizza/assets/135815736/f0d7bbb9-2a14-4d01-83fb-c1de07708aed)|
|Add the json file to the gitignore list to prevent sensitive information being displayed on github.|![api-screen-28](https://github.com/0davidog/PazuzuPizza/assets/135815736/fe312741-72a0-479a-a583-811e78320c8d)|

</details>

### Gitpod

- In order for the app to work correctly with all the installed modules the mock terminal needs to know which modules to install ahead of time.
- To do this we need the file 'requirements.txt'.
- This file will contain a list of modules and their version.
- In my case this is the full list:
```
cachetools==5.3.1
certifi==2023.7.22
charset-normalizer==3.3.0
colorama==0.4.6
google-auth==2.23.2
google-auth-oauthlib==1.1.0
gspread==5.11.3
idna==3.4
maskpass==0.3.7
oauthlib==3.2.2
pyasn1==0.5.0
pyasn1-modules==0.3.0
pyfiglet==1.0.2
requests==2.31.0
requests-oauthlib==1.3.1
rsa==4.9
urllib3==2.0.6
```
Python can populate this list for you automatically with this command:
```
pip3 freeze > requirements.txt
```

### Heroku

The project was deployed on Heroku using Code Institute's mock terminal.

<details><summary>Details for deployment:</summary>
    
|Step|Screen|
|----|------|
|Head over to heroku and log in. Choose 'create new app'.|![heroku-screen-01](https://github.com/0davidog/PazuzuPizza/assets/135815736/116c0385-20ae-47e3-b789-0dd7d0e3510f)|
|Choose a name for your app and your location. Hit 'create app'.|![heroku-screen-02](https://github.com/0davidog/PazuzuPizza/assets/135815736/da56730b-cb2c-4fed-ab72-3685e92aa9f0)|
|Select the 'Settings' tab.|![heroku-screen-04](https://github.com/0davidog/PazuzuPizza/assets/135815736/bfd5280f-1621-425a-a79e-514bbc8a4af2)|
|In Config Vars, reveal config vars.|![heroku-screen-06](https://github.com/0davidog/PazuzuPizza/assets/135815736/7d36657a-721f-40a0-a660-a2664697b5a1)|
|Paste your json file. Make sure the name is the same. |![heroku-screen-07](https://github.com/0davidog/PazuzuPizza/assets/135815736/a532c92e-6ee4-4260-b97b-11cf8b507de8)|
|Down to the Buildpacks section.|![heroku-screen-08](https://github.com/0davidog/PazuzuPizza/assets/135815736/e089db21-c477-44a0-a407-6de488dc8a07)|
|Select 'Add Buildpacks'|![heroku-screen-09](https://github.com/0davidog/PazuzuPizza/assets/135815736/b5df724f-1c07-4dd6-9d00-685833440be7)|
|Add Python buildpack.|![heroku-screen-10](https://github.com/0davidog/PazuzuPizza/assets/135815736/61dfcd4b-8630-4ca8-96df-1a8d890bed5b)|
|Repeat and add nodejs.|![heroku-screen-11](https://github.com/0davidog/PazuzuPizza/assets/135815736/e20ec790-ccbc-4801-89c6-9ae335f442c7)|
|Make sure the order is the same.|![heroku-screen-12](https://github.com/0davidog/PazuzuPizza/assets/135815736/f037c40e-61ee-43a4-8a0e-dc1381eb8c44)|
|Head over to the Deploy tab.|![heroku-screen-13](https://github.com/0davidog/PazuzuPizza/assets/135815736/8bc5cb82-939f-4984-80b0-e9cb1012aa6f)|
|Select Github|![heroku-screen-14](https://github.com/0davidog/PazuzuPizza/assets/135815736/a4ec67be-360e-48ec-968e-8355411cd5ff)|
|You will need to authorize this.|![heroku-screen-15](https://github.com/0davidog/PazuzuPizza/assets/135815736/75382caa-9aba-4b0a-8e51-cce6c37d59f7)|
|Choose your repository.|![heroku-screen-16](https://github.com/0davidog/PazuzuPizza/assets/135815736/8365dac8-2caf-47a5-82df-39c05e4e01a0)|
|Choose your branch in automatic deploys.|![heroku-screen-17](https://github.com/0davidog/PazuzuPizza/assets/135815736/38ce6bee-6c49-4ab4-bb61-9ca1c8519ee8)|
|Confirmation|![heroku-screen-18](https://github.com/0davidog/PazuzuPizza/assets/135815736/6e810e14-641c-4021-9915-d9e9ca6219c9)|
|You can now view your app.|![heroku-screen-19](https://github.com/0davidog/PazuzuPizza/assets/135815736/93a1f38d-f1ab-4948-99b8-a5e7ea53cf10)|

</details>

## Credits

### Content

For the code used to authorize and access Google Drive and Google sheets I followed the Code Institute Love-Sandwiches walkthrough project. This was due to the code dealing with complicated concepts that needed to be written accurately for the whole project to work.

Here's the code used:
```
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pazuzu_pizza')
```

#### Table of Contents

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

### Mentor

Malia Havlicek

### Author

David C. O'Gara 2023

# Pazuzu Pizza

![pazuzu-cover-images](https://github.com/0davidog/PazuzuPizza/assets/135815736/50a329f8-8860-48f1-af60-b152dc235c0e)

Author: David C. O'Gara

Pazuzu Pizza is a command line application. built in python, that enables users an easy way to keep up to date with sales and stock of their buisness. 
The app is created specifically for Pazuzu Pizza, a small pizza counter within a supermarket and offers its users the ability to input sales data and wastages while automating their production plan and offering access to other useful information such as pizza recipies and menu lists.

## Live Site

[Pazuzu Pizza via Heroku](https://pazuzuz-pizza-b36de06442d6.herokuapp.com/)

## Repository

[Pazuzu Pizza Repository on Github](https://github.com/0davidog/PazuzuPizza)

## How to Use

![deployed-screen-01](https://github.com/0davidog/PazuzuPizza/assets/135815736/48196768-f1b3-4c84-8430-8d807d664021)

- The user is first asked to login.
    This is done by choosing one of these pre-made user accounts:
    ![employee-screen](https://github.com/0davidog/PazuzuPizza/assets/135815736/d9a05930-565f-4741-b385-d8340e20d0da)
- The user is then asked to select option. This is done by inputting the option number.
- Selecting 1. 'Display Menu' brings up a list of pizza styles the company makes.
- Selecting 2. 'Input Sales' asks the user to input a number for each pizza.
- Selecting 3. 'Input Disosals' asks user to input disposal number for each pizza ingredient.
- Selecting 4. 'View Production Plan' shows the user to amount of pizzas to be made for todays date..
- Selecting 5. 'View Pizza Recipie' asks the user to choose a pizza by number and then displays the recipie for the chosen pizza.
  
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

- ### Display Menu
- ### Input Sales
- ### Input Disposals
- ### View Production Plan
- ### View Pizza Recipie

## Future Features

- pizza stock
- employee login

## Planning Documentation

Flow chart for 'input sales' function:
![input_sales drawio(1)](https://github.com/0davidog/PazuzuPizza/assets/135815736/aac4bf20-a68b-48a2-96d4-d4d7705c8ad2)

## Data Model

- pizza class?

## Libraries Used

- gspread
- datetime

## Testing

(I have manually tested by doing the following...)
- pep8
- input tests
- local and heroku

### Bugs

- warning once per round

```
C:\Users\David\OneDrive\Documents\00WebDev\pazuzupizza\PazuzuPizza\.venv\Lib\site-packages\gspread\worksheet.py:1069: UserWarning: [Deprecated][in version 6.0.0]: method signature will change to: 'Worksheet.update(value = [[]], range_name=)' arguments 'range_name' and 'values' will swap, values will be mandatory of type: 'list(list(...))'
  warnings.warn(
```

- (error occured because I had Sun in lowercase)
```
Error: An unexpected error occurred - {'code': 400, 'message': "Unable to parse range: 'pizza_production'!NONE2", 'status': 'INVALID_ARGUMENT'}
```
- get stuck in select pizza recipie

### Remaining Bugs

### Validator Testing

PEP8 validator passed with no issues.

![Screenshot 2023-10-18 at 16-38-28 CI Python Linter](https://github.com/0davidog/PazuzuPizza/assets/135815736/e9b9ecbd-7438-463e-a81b-9631506e103a)

[PEP8 Validator/ CI Python Linter](https://pep8ci.herokuapp.com/#)

## Deployment

The project was deployed on Heroku using Code Institute's mock terminal.

## Credits

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

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

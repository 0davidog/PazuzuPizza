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

- The user is first asked to select option. This is done by inputting the option number.
- Selecting 1. 'Display Menu' brings up a list of pizza styles the company makes.
- Selecting 2. 'Input Sales' asks the user to input a number for each pizza.
- Selecting 3. 'Input Disosals' brings up another option choice:
  - Selecting disposal option 1.
  - Selecting disposal option 2.
  - Selecting disposal option 3.
- Selecting 4. 'View Production Plan' shows the user to amount of pizzas to be made for todays date..
- Selecting 5. 'View Pizza Recipie' asks the user to choose a pizza by number and then displays the recipie for the chosen pizza.
  
## Features

- ### Display Menu
- ### Input Sales
- ### Input Disposals
- ### View Production Plan
- ### View Pizza Recipie

## Future Features

- pizza stock
- employee login

## Planning Documentation

Flow charts

## Data Model

- pizza class
- employee class

## Libraries Used

- gspread
- datetime

## Testing

### Bugs

### Remaining Bugs

### Validator Testing

PEP8

## Deployment

The project was deployed on Heroku using Code Institute's mock terminal.

## Credits

Code Institute.

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

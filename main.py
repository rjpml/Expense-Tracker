#Flet is a Python library for building interactive web, desktop, and mobile apps using only Python,
#Without needing HTML, CSS, or JavaScript. It lets you create user interfaces easily.
import flet as ft
import datetime
#For saving and loading our data in a file
import json
#Check if a created or saved file exist
import os
#It allows you to create dictionaries that automatically assign a default value to new keys
from collections import defaultdict

#List that will store all the expense entries
expenses = []
#Track the selected month for filtering
selected_month = "All"
months = ["All", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#Store the expenses
DATA_FILE = "expenses.json"

#Function to load saved expenses from a JSON File
def load_expenses():
    #Check if the data file exists before trying to open it
    if os.path.exists(DATA_FILE):
        #Open the file in read mode
        with open(DATA_FILE, "r") as f:
            #Load the JSON data from the file
            data = json.load(f)
            for item in data:
                #Add the following dictionary to the expenses list
                expenses.append({
                    "title": item["title"],
                    "amount": item["amount"],
                    "category": item["category"],
                    #Convert the string date (e.g. "2025-06-10") to a real date object
                    "date": datetime.datetime.strptime(item["date"], '%Y-%m-%d').date()
                })

#1. 'page' is a parameter
#2. 'ft.Page' is just a hint showing what type of object it is
def main(page: ft.Page):
    page.title = "Expense Tracker"
    page.theme_mode = ft.ThemeMode.DARK
    #Add spacing around the contents of the page
    page.padding = 20
    # Allow the page to scroll automatically if content doesn't fit on screen
    page.scroll = ft.ScrollMode.AUTO

    #Load the expenses that is saved from a JSON File
    load_expenses()


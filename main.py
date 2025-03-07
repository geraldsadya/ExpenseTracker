import argparse
import json
import os
from datetime import datetime


def create_parser():
    #Creating a new parser object with thed desctiptin of tool
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")

    """The dest="command" part means that when a user enters a command, it will be stored in a variable named command"""
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    "The help argument describes what these sub-commands are for."

    #command to add new expense
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, help="Description of the expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount of the expense")
    return parser

def load_data(file_path="expenses.json"):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            #empty or corrupted file here so return an empty list.
            return []
    return data

def save_data(data, file_path="expenses.json"):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def add_expense(description, amount, file_path="expenses.json"):
    expenses = load_data(file_path)#Load existing expenses
    new_id = expenses[-1]["id"] + 1 if expenses else 1

    #Creating the new expense entry with the current date so i have to import data and time
    new_expense = {
        "id": new_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": amount
    }

    #Append and save the data
    expenses.append(new_expense)
    save_data(expenses, file_path)
    print(f"Expense added successfully (ID: {new_id})")

def main():
    parser = create_parser()#Create the argument parser
    args = parser.parse_args() #Parse the arguments from the command line

    #Check which command was used
    if args.command == "hello":
        print("Hello from Expense Tracker!")
    elif args.command == "add":
        add_expense(args.description, args.amount)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

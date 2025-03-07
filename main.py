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

    #command to list all expenses
    list_parser = subparsers.add_parser("list", help="List all expenses")

    #command to delete an expense
    delete_parser = subparsers.add_parser("delete", help="Delete an expense by ID")
    delete_parser.add_argument("--id", type=int, required=True, help="ID of the expense to delete")

    #command to update an expense
    update_parser = subparsers.add_parser("update", help="Update an expense by ID")
    update_parser.add_argument("--id", type=int, required=True, help="ID of the expense to update")
    update_parser.add_argument("--description", help="New description for the expense")
    update_parser.add_argument("--amount", type=float, help="New amount for the expense")

    #command to summarize expenses
    summary_parser = subparsers.add_parser("summary", help="Summarize expenses")
    summary_parser.add_argument("--month", type=int, help="Filter expenses by month (1-12)")

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


def list_expenses(file_path="expenses.json"):
    expenses = load_data(file_path)
    if not expenses:
        print("No expenses recorded.")
        return
    print(f"{'ID':<5} {'Date':<12} {'Description':<20} {'Amount':<10}")
    print("-" * 50)
    for expense in expenses:
        print(f"{expense['id']:<5} {expense['date']:<12} {expense['description']:<20} ${expense['amount']:<10.2f}")


def delete_expense(expense_id, file_path="expenses.json"):
    expenses = load_data(file_path)
    #Find the expense with the given ID
    updated_expenses = [expense for expense in expenses if expense["id"] != expense_id]

    if len(expenses) == len(updated_expenses):
        print(f"No expense found with ID: {expense_id}")
    else:
        save_data(updated_expenses, file_path)
        print(f"Expense deleted successfully (ID: {expense_id})")


def update_expense(expense_id, description=None, amount=None, file_path="expenses.json"):
    expenses = load_data(file_path)
    found = False
    for expense in expenses:
        if expense["id"] == expense_id:
            if description:
                expense["description"] = description
            if amount is not None:  #allow 0 as a valid value
                expense["amount"] = amount
            found = True
            break

    if found:
        save_data(expenses, file_path)
        print(f"Expense updated successfully (ID: {expense_id})")
    else:
        print(f"No expense found with ID: {expense_id}")

def summarize_expenses(month=None, file_path="expenses.json"):
    expenses = load_data(file_path)
    total = 0
    filtered_expenses = expenses

    if month is not None:
        #Filter expenses by month (assumes the date is in "YYYY-MM-DD" format)
        filtered_expenses = [
            expense for expense in expenses
            if datetime.strptime(expense["date"], "%Y-%m-%d").month == month
        ]

    for expense in filtered_expenses:
        total += expense["amount"]
    if month is None:
        print(f"Total expenses: ${total:.2f}")
    else:
        print(f"Total expenses for month {month}: ${total:.2f}")



def main():
    parser = create_parser()#Create the argument parser
    args = parser.parse_args() #Parse the arguments from the command line

    #Check which command was used
    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "list":
        list_expenses()
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)
    elif args.command == "summary":
        summarize_expenses(args.month)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

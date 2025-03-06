import argparse
import json
import os


def create_parser():
    #Creating a new parser object with thed desctiptin of tool
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")

    """The dest="command" part means that when a user enters a command, it will be stored in a variable named command"""
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    "The help argument describes what these sub-commands are for."

    #test:hello (just to test the CLI)
    hello_parser = subparsers.add_parser("hello", help="Say hello")
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

def main():
    parser = create_parser()#Create the argument parser
    args = parser.parse_args() #Parse the arguments from the command line

    #Check which command was used
    if args.command == "hello":
        print("Hello from Expense Tracker!")
    else:
        #If no command or an unrecognized command is provided, print help
        parser.print_help()

if __name__ == "__main__":
    main()

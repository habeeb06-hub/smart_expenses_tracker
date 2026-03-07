#smart expenses tracker project
import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        date = datetime.now().strftime("%Y-%m-%d")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, date])

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount!")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n--- All Expenses ---")
            for row in reader:
                print("Amount:", row[0], "| Category:", row[1], "| Date:", row[2])

    except FileNotFoundError:
        print("No expenses found.")


def show_total():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                total += float(row[0])

        print(f"\nTotal Expense: Rs.{total}")

    except FileNotFoundError:
        print("No expenses found.")


def category_total():
    totals = {}

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                category = row[1]
                amount = float(row[0])

                if category in totals:
                    totals[category] += amount
                else:
                    totals[category] = amount

        print("\n--- Category Wise Total ---")

        for category, amount in totals.items():
            print(category, ":", amount)

    except FileNotFoundError:
        print("No expenses found.")


def delete_expense():
    expenses = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                expenses.append(row)

        print("\n--- Expenses ---")
        for i, row in enumerate(expenses):
            print(i + 1, "|", row)

        num = int(input("Enter expense number to delete: "))

        if 1 <= num <= len(expenses):
            expenses.pop(num - 1)

            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(expenses)

            print("Expense deleted!")

        else:
            print("Invalid number")

    except FileNotFoundError:
        print("No expenses found.")


while True:

    print("\n--- Smart Expense Tracker ---")
    print("1 Add Expense")
    print("2 View Expenses")
    print("3 Show Total")
    print("4 Category Wise Total")
    print("5 Delete Expense")
    print("6 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        category_total()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
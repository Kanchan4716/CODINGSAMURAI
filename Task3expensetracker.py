import json

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def add_expense(expenses, categories):
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount: "))
    
    print("Expense Categories:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    category_index = int(input("Select a category by number: ")) - 1
    category = categories[category_index]
    
    description = input("Enter a brief description: ")

    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully.")

def list_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for i, expense in enumerate(expenses, start=1):
            print(f"Expense #{i}:")
            print(f"Date: {expense['date']}")
            print(f"Amount: ${expense['amount']:.2f}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print()

def calculate_total(expenses):
    total = sum(expense['amount'] for expense in expenses)
    return total

def generate_monthly_report(expenses, month):
    monthly_expenses = [expense for expense in expenses if expense['date'].startswith(month)]
    if not monthly_expenses:
        print(f"No expenses recorded for {month}.")
    else:
        total = calculate_total(monthly_expenses)
        print(f"Monthly Report for {month}:")
        print(f"Total Expenses: {total:.2f}")
        print("Expense Breakdown:")
        for category in set(expense['category'] for expense in monthly_expenses):
            category_total = sum(expense['amount'] for expense in monthly_expenses if expense['category'] == category)
            print(f"{category}: ${category_total:.2f}")

def main():
    expenses = load_expenses()
    categories = ["Groceries", "Transportation", "Entertainment", "Other"]

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses")
        print("4. Generate Monthly Report")
        print("5. Save and Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            add_expense(expenses, categories)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            total = calculate_total(expenses)
            print(f"Total Expenses: {total:.2f}")
        elif choice == "4":
            month = input("Enter the month (YYYY-MM): ")
            generate_monthly_report(expenses, month)
        elif choice == "5":
            save_expenses(expenses)
            print("Expense data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

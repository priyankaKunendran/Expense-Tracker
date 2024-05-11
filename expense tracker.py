import sqlite3

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY, date TEXT, amount REAL, category TEXT)''')
    conn.commit()
    conn.close()

# Function to add an expense
def add_expense(date, amount, category):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (date, amount, category) VALUES (?, ?, ?)", (date, amount, category))
    conn.commit()
    conn.close()

# Function to retrieve expenses
def get_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    conn.close()
    return expenses

# Function to retrieve expenses by category
def get_expenses_by_category(category):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT * FROM expenses WHERE category=?", (category,))
    expenses = c.fetchall()
    conn.close()
    return expenses

# Function to calculate total expenses
def calculate_total_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT SUM(amount) FROM expenses")
    total_expenses = c.fetchone()[0]
    conn.close()
    return total_expenses

# Function to main menu
def main_menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Expenses by Category")
    print("4. Calculate Total Expenses")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

# Function to add expense
def add_expense_menu():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    add_expense(date, amount, category)
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    expenses = get_expenses()
    for expense in expenses:
        print(expense)

# Function to view expenses by category
def view_expenses_by_category():
    category = input("Enter category: ")
    expenses = get_expenses_by_category(category)
    for expense in expenses:
        print(expense)

# Function to calculate total expenses
def calculate_total_expenses_menu():
    total_expenses = calculate_total_expenses()
    print("Total expenses: $", total_expenses)

# Main function
def main():
    initialize_database()
    while True:
        choice = main_menu()
        if choice == '1':
            add_expense_menu()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_expenses_by_category()
        elif choice == '4':
            calculate_total_expenses_menu()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

from db import cursor, conn
from datetime import datetime
from tabulate import tabulate


def add_transactions(user_id, t_type, category, amount, date, note=None):
    query = """
    INSERT INTO transactions (user_id, type, category, amount, date, note)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (user_id, t_type, category, amount, date, note)
    cursor.execute(query, values)
    conn.commit()
    print("Transaction added sucessfully.")


def get_transactions():
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()

    headers = ["ID", "User ID", "Type", "Category", "Amount", "Date", "Description"]
    print(tabulate(rows, headers, tablefmt="psql"))


def update_transactions(transaction_id, new_amount):
    query = """
        UPDATE transactions SET amount= %s  where id = %s
    """
    cursor.execute(query, (new_amount, transaction_id))
    conn.commit()

    print("Transaction updated sucessfully.")


def delete_transactions(transaction_id):
    query = """
    DELETE FROM transactions WHERE id = %s
    """
    cursor.execute(query, (transaction_id,))
    conn.commit()
    print("Transaction deleted successfully!")


def main():
    while True:
        print("\n====== Personal Finance Tracker CLI ======")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            user_id = int(input("Enter user ID: "))
            t_type = input("Enter type (income/expense): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            date_str = input("Enter date (YYYY-MM-DD): ")
            note = input("Enter note (optional): ") or None

            try:
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                add_transactions(user_id, t_type, category, amount, date, note)
            except ValueError:
                print("Invalid date format.")

        elif choice == "2":
            get_transactions()

        elif choice == "3":
            transaction_id = int(input("Enter transaction ID to update: "))
            new_amount = float(input("Enter new amount: "))
            update_transactions(transaction_id, new_amount)

        elif choice == "4":
            transaction_id = int(input("Enter transaction ID to delete: "))
            delete_transactions(transaction_id)

        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    main()

import json


class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

    def to_dict(self):
        return {
            "description": self.description,
            "amount": self.amount,
            "category": self.category
        }


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print(f"Added: {expense.description} - {expense.amount} ({expense.category})")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        for i, expense in enumerate(self.expenses):
            print(f"{i}. {expense.description} - {expense.amount} ({expense.category})")

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"Deleted: {removed.description}")
        else:
            print("Invalid expense index.")

    def save_to_file(self, filename="data.json"):
        data = [expense.to_dict() for expense in self.expenses]
        with open(filename, "w") as file:
            json.dump(data, file)
        print("Expenses saved.")

    def load_from_file(self, filename="data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for item in data:
                    expense = Expense(item["description"], item["amount"], item["category"])
                    self.expenses.append(expense)
            print("Expenses loaded.")
        except FileNotFoundError:
            print("No existing data file found. Starting fresh.")


tracker = ExpenseTracker()
tracker.load_from_file()
tracker.add_expense(Expense("Lunch", 1500, "Food"))
tracker.view_expenses()
tracker.save_to_file()
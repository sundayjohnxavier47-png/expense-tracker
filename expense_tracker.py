class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

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

tracker = ExpenseTracker()
tracker.add_expense(Expense("Lunch", 1500, "Food"))
tracker.add_expense(Expense("Uber", 2000, "Transport"))
tracker.view_expenses()
tracker.delete_expense(0)
tracker.view_expenses()
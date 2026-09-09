from expense_tracker import Expense, ExpenseTracker

def test_add_expense():
    tracker = ExpenseTracker()
    tracker.add_expense(Expense("Lunch", 1500, "Food"))
    assert len(tracker.expenses) == 1
    assert tracker.expenses[0].description == "Lunch"

def test_delete_expense():
    tracker = ExpenseTracker()
    tracker.add_expense(Expense("Lunch", 1500, "Food"))
    tracker.delete_expense(0)
    assert len(tracker.expenses) == 0

def test_to_dict():
    expense = Expense("Lunch", 1500, "Food")
    data = expense.to_dict()
    assert data == {"description": "Lunch", "amount": 1500, "category": "Food"}
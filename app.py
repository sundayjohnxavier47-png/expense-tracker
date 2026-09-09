from flask import Flask, render_template, request, redirect, url_for
from expense_tracker import Expense, ExpenseTracker

app = Flask(__name__)
tracker = ExpenseTracker()
tracker.load_from_file()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        description = request.form["description"]
        amount = float(request.form["amount"])
        category = request.form["category"]
        tracker.add_expense(Expense(description, amount, category))
        tracker.save_to_file()
        return redirect(url_for("index"))

    total = sum(expense.amount for expense in tracker.expenses)
    return render_template("index.html", expenses=tracker.expenses, total=total)

@app.route("/delete/<int:index>")
def delete(index):
    tracker.delete_expense(index)
    tracker.save_to_file()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)